/*** In The Name of Allah ***/
package srctoolkit.janalysis.dg.cfg;


import srctoolkit.janalysis.utils.Logger;
import srctoolkit.janalysis.common.antlrparser.JavaBaseVisitor;
import srctoolkit.janalysis.common.antlrparser.JavaLexer;
import srctoolkit.janalysis.common.antlrparser.JavaParser;
import srctoolkit.janalysis.dg.DEPEdge;
import srctoolkit.janalysis.dg.DEPNode;
import srctoolkit.janalysis.common.graph.Digraph;
import srctoolkit.janalysis.common.graph.Edge;
import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.misc.Interval;
import org.antlr.v4.runtime.tree.ParseTree;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.*;

/**
 * A Control Flow Graph (CFG) builder for Java programs.
 * A Java parser generated via ANTLRv4 is used for this purpose.
 * This implementation is based on ANTLRv4's Visitor pattern.
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class CFGBuilder {

	public static List<ControlFlowGraph> buildWithCode(String code) throws IOException {
		Logger.info("Parsing source code ... ");
		ANTLRInputStream input = new ANTLRInputStream(code);
		JavaLexer lexer = new JavaLexer(input);
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		JavaParser parser = new JavaParser(tokens);
		ParseTree parseTree = parser.compilationUnit();
		return build(parseTree);
	}
	
	/**
	 * ‌Build and return the Control Flow Graph (CFG) for the given Java source file.
	 */
	public static List<ControlFlowGraph> build(String file) throws IOException {
		Logger.info("Parsing source file ... ");
		InputStream inFile = new FileInputStream(file);
		ANTLRInputStream input = new ANTLRInputStream(inFile);
		JavaLexer lexer = new JavaLexer(input);
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		JavaParser parser = new JavaParser(tokens);
		ParseTree parseTree = parser.compilationUnit();
		return build(parseTree);
	}
	
	/**
	 * ‌Build and return the Control Flow Graph (CFG) for the given Parse-Tree.
	 * The 'ctxProps' map includes contextual-properties for particular nodes 
	 * in the parse-tree, which can be used for linking this graph with other 
	 * graphs by using the same parse-tree and the same contextual-properties.
	 */
	public static List<ControlFlowGraph> build(ParseTree tree) {
		Digraph<DEPNode, CFEdge> wholeCFG = new Digraph<>();
		Map<DEPNode, List<DEPNode>> entry2params = new HashMap<>();
		ControlFlowVisitor visitor = new ControlFlowVisitor(wholeCFG, entry2params);
		visitor.visit(tree);

		return splitGraph(wholeCFG, entry2params);
	}

	public static List<ControlFlowGraph> splitGraph(Digraph<DEPNode, CFEdge> wholeCFG, Map<DEPNode, List<DEPNode>> entry2params) {
		List<ControlFlowGraph> cfgs = new ArrayList<>();
		for (Map.Entry<DEPNode, List<DEPNode>> entry: entry2params.entrySet()) {
			DEPNode methodEntry = entry.getKey();
			List<DEPNode> params = entry.getValue();
			ControlFlowGraph cfg = new ControlFlowGraph(methodEntry.getCode());
			cfg.setEntry(methodEntry);
//			cfg.setParams(params);
			cfgs.add(cfg);

			Deque<DEPNode> waiting = new ArrayDeque<>();
			Set<DEPNode> visitedNodes = new HashSet<>();
			cfg.addVertex(methodEntry);
			waiting.push(methodEntry);
			visitedNodes.add(methodEntry);
			while (!waiting.isEmpty()) {
				DEPNode current = waiting.pop();
				Iterator<Edge<DEPNode, CFEdge>> outEdges = wholeCFG.outgoingEdgesIterator(current);
				while (outEdges.hasNext()) {
					Edge<DEPNode, CFEdge> edge = outEdges.next();
					if (!visitedNodes.contains(edge.target)) {
						cfg.addVertex(edge.target);
						waiting.push(edge.target);
						visitedNodes.add(edge.target);
					}
					if (visitedNodes.contains(edge.target))
						cfg.addEdge(edge);
				}
			}
		}
		return cfgs;
	}
	
	/**
	 * Visitor-class which constructs the CFG by walking the parse-tree.
	 */
	private static class ControlFlowVisitor extends JavaBaseVisitor<Void> {
		
		private Digraph<DEPNode, CFEdge> cfg;
		private Map<DEPNode, List<DEPNode>> entry2params;
		private Deque<DEPNode> preNodes;
		private Deque<String> preEdges;
		private Deque<Block> loopBlocks;
		private List<Block> labeledBlocks;
		private Deque<Block> tryBlocks;

		private Queue<DEPNode> casesQueue;
		private boolean dontPop;
		private Deque<String> classNames;

		private DEPNode preRetForTry = null; // edge case of return statement in try block 

		public ControlFlowVisitor(Digraph<DEPNode, CFEdge> cfg, Map<DEPNode, List<DEPNode>> entry2params) {
			preNodes = new ArrayDeque<>();
			preEdges = new ArrayDeque<>();
			loopBlocks = new ArrayDeque<>();
			labeledBlocks = new ArrayList<>();
			tryBlocks = new ArrayDeque<>();
			casesQueue = new ArrayDeque<>();
			classNames = new ArrayDeque<>();
			dontPop = false;
			this.cfg = cfg;
			this.entry2params = entry2params;
			//

		}

		/**
		 * Reset all data-structures and flags for visiting a new method declaration.
		 */
		private void init() {
			preNodes.clear();
			preEdges.clear();
			loopBlocks.clear();
			labeledBlocks.clear();
			tryBlocks.clear();
			dontPop = false;
		}
		
		/**
		 * Add contextual properties to the given node.
		 * This will first check to see if there is any property for the 
		 * given context, and if so, the property will be added to the node.
		 */
		private void addContextualProperty(DEPNode node, ParserRuleContext ctx) {
			node.setRuleCtx(ctx);
		}
		
		@Override
		public Void visitPackageDeclaration(JavaParser.PackageDeclarationContext ctx) {
			// packageDeclaration :  annotation* 'package' qualifiedName ';'
//			cfg.setPackage(ctx.qualifiedName().getText());
			return null;
		}

		@Override
		public Void visitClassDeclaration(JavaParser.ClassDeclarationContext ctx) {
			// classDeclaration 
			//   :  'class' Identifier typeParameters? 
			//      ('extends' typeType)? ('implements' typeList)? classBody
			classNames.push(ctx.Identifier().getText());
			visit(ctx.classBody());
			classNames.pop();
			return null;
		}

		@Override
		public Void visitEnumDeclaration(JavaParser.EnumDeclarationContext ctx) {
			// Just ignore enums for now ...
			return null;
		}
		
		@Override
		public Void visitInterfaceDeclaration(JavaParser.InterfaceDeclarationContext ctx) {
			// Just ignore interfaces for now ...
			return null;
		}
		
		@Override
		public Void visitClassBodyDeclaration(JavaParser.ClassBodyDeclarationContext ctx) {
			// classBodyDeclaration :  ';'  |  'static'? block  |  modifier* memberDeclaration
			if (ctx.block() != null) {
				init();
				//
				DEPNode block = new DEPNode();
				entry2params.put(block, new ArrayList<>());
				if (ctx.getChildCount() == 2 && ctx.getChild(0).getText().equals("static")) {
					block.setLineOfCode(ctx.getStart().getLine());
					block.setCode("static");
				} else {
					block.setLineOfCode(-1);
					block.setCode("block");
				}
				addContextualProperty(block, ctx);
				cfg.addVertex(block);
				//
				block.setProperty("name", "static-block");
				block.setProperty("class", classNames.peek());
				//
				preNodes.push(block);
				preEdges.push(CFEdge.EPSILON);
			}
			return visitChildren(ctx);
		}

		@Override
		public Void visitConstructorDeclaration(JavaParser.ConstructorDeclarationContext ctx) {
			// Identifier formalParameters ('throws' qualifiedNameList)?  constructorBody
			init();
			//
			DEPNode entry = new DEPNode();
			List<DEPNode> params = new ArrayList<>();
			entry2params.put(entry, params);
			entry.setLineOfCode(ctx.getStart().getLine());
			entry.setCode(ctx.Identifier().getText() + ' ' + getOriginalCodeText(ctx.formalParameters()));
			addContextualProperty(entry, ctx);
			cfg.addVertex(entry);
			//
			entry.setProperty("name", ctx.Identifier().getText());
			entry.setProperty("class", classNames.peek());
			//

			if (ctx.formalParameters().formalParameterList() != null) {
				for (JavaParser.FormalParameterContext prm :
						ctx.formalParameters().formalParameterList().formalParameter()) {
					DEPNode param = new DEPNode();
					param.setLineOfCode(prm.getStart().getLine());
					param.setCode(getOriginalCodeText(prm));
					addContextualProperty(param, prm);
					param.setProperty("type", prm.typeType().getText());
					param.setProperty("name", prm.variableDeclaratorId().Identifier().getText());
					params.add(param);
				}
				JavaParser.LastFormalParameterContext lastParam = ctx.formalParameters().formalParameterList().lastFormalParameter();
				if (lastParam != null) {
					DEPNode param = new DEPNode();
					param.setLineOfCode(lastParam.getStart().getLine());
					param.setCode(getOriginalCodeText(lastParam));
					addContextualProperty(param, lastParam);
					param.setProperty("type", lastParam.typeType().getText());
					param.setProperty("name", lastParam.variableDeclaratorId().Identifier().getText());
					params.add(param);
				}
			}

			preNodes.push(entry);
			preEdges.push(CFEdge.EPSILON);
			return visitChildren(ctx);
		}

		@Override
		public Void visitMethodDeclaration(JavaParser.MethodDeclarationContext ctx) {
			// methodDeclaration :
			//   (typeType|'void') Identifier formalParameters ('[' ']')*
			//     ('throws' qualifiedNameList)?  ( methodBody | ';' )
			init();
			//
			DEPNode entry = new DEPNode();
			List<DEPNode> params = new ArrayList<>();
			entry2params.put(entry, params);
			entry.setLineOfCode(ctx.getStart().getLine());
			String retType = "void";
			if (ctx.typeType() != null)
				retType = ctx.typeType().getText();
			String args = getOriginalCodeText(ctx.formalParameters());
			entry.setCode(retType + " " + ctx.Identifier() + args);
			addContextualProperty(entry, ctx);
			cfg.addVertex(entry);
			//
			entry.setProperty("name", ctx.Identifier().getText());
			entry.setProperty("class", classNames.peek());
			entry.setProperty("type", retType);
			//

			if (ctx.formalParameters().formalParameterList() != null) {
				for (JavaParser.FormalParameterContext prm :
						ctx.formalParameters().formalParameterList().formalParameter()) {
					DEPNode param = new DEPNode();
					param.setLineOfCode(prm.getStart().getLine());
					param.setCode(getOriginalCodeText(prm));
					addContextualProperty(param, prm);
					param.setProperty("type", prm.typeType().getText());
					param.setProperty("name", prm.variableDeclaratorId().Identifier().getText());
					params.add(param);
				}
				JavaParser.LastFormalParameterContext lastParam = ctx.formalParameters().formalParameterList().lastFormalParameter();
				if (lastParam != null) {
					DEPNode param = new DEPNode();
					param.setLineOfCode(lastParam.getStart().getLine());
					param.setCode(getOriginalCodeText(lastParam));
					addContextualProperty(param, lastParam);
					param.setProperty("type", lastParam.typeType().getText());
					param.setProperty("name", lastParam.variableDeclaratorId().Identifier().getText());
					params.add(param);
				}
			}

			preNodes.push(entry);
			preEdges.push(CFEdge.EPSILON);
			return visitChildren(ctx);
		}

		@Override
		public Void visitStatementExpression(JavaParser.StatementExpressionContext ctx) {
			// statementExpression ';'
			DEPNode expr = new DEPNode();
			expr.setLineOfCode(ctx.getStart().getLine());
			expr.setCode(getOriginalCodeText(ctx));
			//
			Logger.debug(expr.getLineOfCode() + ": " + expr.getCode());
			//
			addContextualProperty(expr, ctx);
			addNodeAndPreEdge(expr);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(expr);
			return null;
		}
		
		@Override
		public Void visitLocalVariableDeclaration(JavaParser.LocalVariableDeclarationContext ctx) {
			// localVariableDeclaration :  variableModifier* typeType variableDeclarators
			DEPNode declr = new DEPNode();
			declr.setLineOfCode(ctx.getStart().getLine());
			declr.setCode(getOriginalCodeText(ctx));
			addContextualProperty(declr, ctx);
			addNodeAndPreEdge(declr);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(declr);
			return null;
		}

		@Override
		public Void visitIfStatement(JavaParser.IfStatementContext ctx) {
			// 'if' parExpression statement ('else' statement)?
			DEPNode ifNode = new DEPNode();
			ifNode.setLineOfCode(ctx.getStart().getLine());
			ifNode.setCode("if " + getOriginalCodeText(ctx.parExpression()));
			addContextualProperty(ifNode, ctx);
			addNodeAndPreEdge(ifNode);
			//
			preEdges.push(CFEdge.TRUE);
			preNodes.push(ifNode);
			//
			visit(ctx.statement(0));
			//
			DEPNode endif = new DEPNode();
			endif.setLineOfCode(-1);
			endif.setCode("end-if:" + ifNode.getLineOfCode());
			addNodeAndPreEdge(endif);
			//
			if (ctx.statement().size() == 1) { // if without else
				cfg.addEdge(new Edge<>(ifNode, new CFEdge(CFEdge.FALSE), endif));
			} else {  //  if with else
				preEdges.push(CFEdge.FALSE);
				preNodes.push(ifNode);
				visit(ctx.statement(1));
				popAddPreEdgeTo(endif);
			}
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(endif);
			return null;
		}

		@Override
		public Void visitForStatement(JavaParser.ForStatementContext ctx) {
			// 'for' '(' forControl ')' statement
			//  First, we should check type of for-loop ...
			if (ctx.forControl().enhancedForControl() != null) {
				// This is a for-each loop;
				//   enhancedForControl: 
				//     variableModifier* typeType variableDeclaratorId ':' expression
				DEPNode forExpr = new DEPNode();
				forExpr.setLineOfCode(ctx.forControl().getStart().getLine());
				forExpr.setCode("for (" + getOriginalCodeText(ctx.forControl()) + ")");
				addContextualProperty(forExpr, ctx.forControl().enhancedForControl());
				addNodeAndPreEdge(forExpr);
				//
				DEPNode forEnd = new DEPNode();
				forEnd.setLineOfCode(-1);
				forEnd.setCode("end-for:" + forExpr.getLineOfCode());
				cfg.addVertex(forEnd);
				cfg.addEdge(new Edge<>(forExpr, new CFEdge(CFEdge.FALSE), forEnd));
				//
				preEdges.push(CFEdge.TRUE);
				preNodes.push(forExpr);
				//
				loopBlocks.push(new Block(forExpr, forEnd));
				visit(ctx.statement());
				loopBlocks.pop();
				popAddPreEdgeTo(forExpr);
				//
				preEdges.push(CFEdge.EPSILON);
				preNodes.push(forEnd);
			} else {
				// It's a traditional for-loop: 
				//   forInit? ';' expression? ';' forUpdate?
				DEPNode forInit = null;
				if (ctx.forControl().forInit() != null) { // non-empty init
					forInit = new DEPNode();
					forInit.setLineOfCode(ctx.forControl().forInit().getStart().getLine());
					forInit.setCode(getOriginalCodeText(ctx.forControl().forInit()));
					addContextualProperty(forInit, ctx.forControl().forInit());
					addNodeAndPreEdge(forInit);
				}
				// for-expression
				DEPNode forExpr = new DEPNode();
				if (ctx.forControl().expression() == null) {
					forExpr.setLineOfCode(ctx.forControl().getStart().getLine());
					forExpr.setCode("for ( ; )");
				} else {
					forExpr.setLineOfCode(ctx.forControl().expression().getStart().getLine());
					forExpr.setCode("for (" + getOriginalCodeText(ctx.forControl().expression()) + ")");
				}
				addContextualProperty(forExpr, ctx.forControl().expression());
				cfg.addVertex(forExpr);
				if (forInit != null)
					cfg.addEdge(new Edge<>(forInit, new CFEdge(CFEdge.EPSILON), forExpr));
				else
					popAddPreEdgeTo(forExpr);
				// for-update
				DEPNode forUpdate = new DEPNode();
				if (ctx.forControl().forUpdate() == null) { // empty for-update
					forUpdate.setCode(" ; ");
					forUpdate.setLineOfCode(ctx.forControl().getStart().getLine());
				} else {
					forUpdate.setCode(getOriginalCodeText(ctx.forControl().forUpdate()));
					forUpdate.setLineOfCode(ctx.forControl().forUpdate().getStart().getLine());
				}
				addContextualProperty(forUpdate, ctx.forControl().forUpdate());
				cfg.addVertex(forUpdate);
				//
				DEPNode forEnd = new DEPNode();
				forEnd.setLineOfCode(-1);
				forEnd.setCode("end-for:" + forExpr.getLineOfCode());
				cfg.addVertex(forEnd);
				cfg.addEdge(new Edge<>(forExpr, new CFEdge(CFEdge.FALSE), forEnd));
				//
				preEdges.push(CFEdge.TRUE);
				preNodes.push(forExpr);
				loopBlocks.push(new Block(forUpdate, forEnd)); // NOTE: start is 'forUpdate'
				visit(ctx.statement());
				loopBlocks.pop();
				popAddPreEdgeTo(forUpdate);
				cfg.addEdge(new Edge<>(forUpdate, new CFEdge(CFEdge.EPSILON), forExpr));
				//
				preEdges.push(CFEdge.EPSILON);
				preNodes.push(forEnd);
			}
			return null;
		}

		@Override
		public Void visitWhileStatement(JavaParser.WhileStatementContext ctx) {
			// 'while' parExpression statement
			DEPNode whileNode = new DEPNode();
			whileNode.setLineOfCode(ctx.getStart().getLine());
			whileNode.setCode("while " + getOriginalCodeText(ctx.parExpression()));
			addContextualProperty(whileNode, ctx);
			addNodeAndPreEdge(whileNode);
			//
			DEPNode endwhile = new DEPNode();
			endwhile.setLineOfCode(-1);
			endwhile.setCode("end-while:" + whileNode.getLineOfCode());
			cfg.addVertex(endwhile);
			cfg.addEdge(new Edge<>(whileNode, new CFEdge(CFEdge.FALSE), endwhile));
			//
			preEdges.push(CFEdge.TRUE);
			preNodes.push(whileNode);
			loopBlocks.push(new Block(whileNode, endwhile));
			visit(ctx.statement());
			loopBlocks.pop();
			popAddPreEdgeTo(whileNode);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(endwhile);
			return null;
		}

		@Override
		public Void visitDoWhileStatement(JavaParser.DoWhileStatementContext ctx) {
			// 'do' statement 'while' parExpression ';'
			DEPNode doNode = new DEPNode();
			doNode.setLineOfCode(ctx.getStart().getLine());
			doNode.setCode("do");
			addNodeAndPreEdge(doNode);
			//
			DEPNode whileNode = new DEPNode();
			whileNode.setLineOfCode(ctx.parExpression().getStart().getLine());
			whileNode.setCode("while " + getOriginalCodeText(ctx.parExpression()));
			addContextualProperty(whileNode, ctx);
			cfg.addVertex(whileNode);
			//
			DEPNode doWhileEnd = new DEPNode();
			doWhileEnd.setLineOfCode(-1);
			doWhileEnd.setCode("end-do-while:" + whileNode.getLineOfCode());
			cfg.addVertex(doWhileEnd);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(doNode);
			loopBlocks.push(new Block(whileNode, doWhileEnd));
			visit(ctx.statement());
			loopBlocks.pop();
			popAddPreEdgeTo(whileNode);
			cfg.addEdge(new Edge<>(whileNode, new CFEdge(CFEdge.TRUE), doNode));
			cfg.addEdge(new Edge<>(whileNode, new CFEdge(CFEdge.FALSE), doWhileEnd));
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(doWhileEnd);
			return null;
		}

		@Override
		public Void visitSwitchStatement(JavaParser.SwitchStatementContext ctx) {
			// 'switch' parExpression '{' switchBlockStatementGroup* switchLabel* '}'
			DEPNode switchNode = new DEPNode();
			switchNode.setLineOfCode(ctx.getStart().getLine());
			switchNode.setCode("switch " + getOriginalCodeText(ctx.parExpression()));
			addContextualProperty(switchNode, ctx);
			addNodeAndPreEdge(switchNode);
			//
			DEPNode endSwitch = new DEPNode();
			endSwitch.setLineOfCode(-1);
			endSwitch.setCode("end-switch:" + switchNode.getLineOfCode());
			cfg.addVertex(endSwitch);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(switchNode);
			loopBlocks.push(new Block(switchNode, endSwitch));
			//
			DEPNode preCase = null;
			for (JavaParser.SwitchBlockStatementGroupContext grp: ctx.switchBlockStatementGroup()) {
				// switchBlockStatementGroup :  switchLabel+ blockStatement+
				preCase = visitSwitchLabels(grp.switchLabel(), preCase);
				for (JavaParser.BlockStatementContext blk: grp.blockStatement())
					visit(blk);
			}
			preCase = visitSwitchLabels(ctx.switchLabel(), preCase);
			loopBlocks.pop();
			popAddPreEdgeTo(endSwitch);
			if (preCase != null)
				cfg.addEdge(new Edge<>(preCase, new CFEdge(CFEdge.FALSE), endSwitch));
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(endSwitch);
			return null;
		}

		private DEPNode visitSwitchLabels(List<JavaParser.SwitchLabelContext> list, DEPNode preCase) {
			//  switchLabel :  'case' constantExpression ':'  |  'case' enumConstantName ':'  |  'default' ':'
			DEPNode caseStmnt = preCase;
			for (JavaParser.SwitchLabelContext ctx: list) {
				caseStmnt = new DEPNode();
				caseStmnt.setLineOfCode(ctx.getStart().getLine());
				caseStmnt.setCode(getOriginalCodeText(ctx));
				cfg.addVertex(caseStmnt);
				if (dontPop)
					dontPop = false;
				else
					cfg.addEdge(new Edge<>(preNodes.pop(), new CFEdge(preEdges.pop()), caseStmnt));
				if (preCase != null)
					cfg.addEdge(new Edge<>(preCase, new CFEdge(CFEdge.FALSE), caseStmnt));
				if (ctx.getStart().getText().equals("default")) {
					preEdges.push(CFEdge.EPSILON);
					preNodes.push(caseStmnt);
					caseStmnt = null;
				} else { // any other case ...
					dontPop = true;
					casesQueue.add(caseStmnt);
					preCase = caseStmnt;
				}
			}
			return caseStmnt;
		}

		@Override
		public Void visitLabelStatement(JavaParser.LabelStatementContext ctx) {
			// Identifier ':' statement
			// For each visited label-block, a Block object is created with 
			// the the current node as the start, and a dummy node as the end.
			// The newly created label-block is stored in an ArrayList of Blocks.
			DEPNode labelNode = new DEPNode();
			labelNode.setLineOfCode(ctx.getStart().getLine());
			labelNode.setCode(ctx.Identifier() + ": ");
			addContextualProperty(labelNode, ctx);
			addNodeAndPreEdge(labelNode);
			//
			DEPNode endLabelNode = new DEPNode();
			endLabelNode.setLineOfCode(-1);
			endLabelNode.setCode("end-label:" + labelNode.getLineOfCode());
			cfg.addVertex(endLabelNode);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(labelNode);
			labeledBlocks.add(new Block(labelNode, endLabelNode, ctx.Identifier().getText()));
			visit(ctx.statement());
			popAddPreEdgeTo(endLabelNode);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(endLabelNode);
			return null;
		}

		@Override
		public Void visitReturnStatement(JavaParser.ReturnStatementContext ctx) {
			// 'return' expression? ';'
			DEPNode ret = new DEPNode();
			ret.setLineOfCode(ctx.getStart().getLine());
			ret.setCode(getOriginalCodeText(ctx));
			addContextualProperty(ret, ctx);
			addNodeAndPreEdge(ret);
			dontPop = true;
			return null;
		}

		@Override
		public Void visitBreakStatement(JavaParser.BreakStatementContext ctx) {
			// 'break' Identifier? ';'
			// if a label is specified, search for the corresponding block in the labels-list,
			// and create an epsilon edge to the end of the labeled-block; else
			// create an epsilon edge to the end of the loop-block on top of the loopBlocks stack.
			DEPNode breakNode = new DEPNode();
			breakNode.setLineOfCode(ctx.getStart().getLine());
			breakNode.setCode(getOriginalCodeText(ctx));
			addContextualProperty(breakNode, ctx);
			addNodeAndPreEdge(breakNode);
			if (ctx.Identifier() != null) {
				// a label is specified
				for (Block block: labeledBlocks) {
					if (block.label.equals(ctx.Identifier().getText())) {
						cfg.addEdge(new Edge<>(breakNode, new CFEdge(CFEdge.EPSILON), block.end));
						break;
					}
				}
			} else {
				// no label
				Block block = loopBlocks.peek();
				cfg.addEdge(new Edge<>(breakNode, new CFEdge(CFEdge.EPSILON), block.end));
			}
			dontPop = true;
			return null;
		}

		@Override
		public Void visitContinueStatement(JavaParser.ContinueStatementContext ctx) {
			// 'continue' Identifier? ';'
			// if a label is specified, search for the corresponding block in the labels-list,
			// and create an epsilon edge to the start of the labeled-block; else
			// create an epsilon edge to the start of the loop-block on top of the loopBlocks stack.
			DEPNode continueNode = new DEPNode();
			continueNode.setLineOfCode(ctx.getStart().getLine());
			continueNode.setCode(getOriginalCodeText(ctx));
			addContextualProperty(continueNode, ctx);
			addNodeAndPreEdge(continueNode);
			if (ctx.Identifier() != null) {  
				// a label is specified
				for (Block block: labeledBlocks) {
					if (block.label.equals(ctx.Identifier().getText())) {
						cfg.addEdge(new Edge<>(continueNode, new CFEdge(CFEdge.EPSILON), block.start));
						break;
					}
				}
			} else {  
				// no label
				Block block = loopBlocks.peek();
				cfg.addEdge(new Edge<>(continueNode, new CFEdge(CFEdge.EPSILON), block.start));
			}
			dontPop = true;
			return null;
		}

		@Override
		public Void visitSynchBlockStatement(JavaParser.SynchBlockStatementContext ctx) {
			// 'synchronized' parExpression block
			DEPNode syncStmt = new DEPNode();
			syncStmt.setLineOfCode(ctx.getStart().getLine());
			syncStmt.setCode("synchronized " + getOriginalCodeText(ctx.parExpression()));
			addContextualProperty(syncStmt, ctx);
			addNodeAndPreEdge(syncStmt);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(syncStmt);
			visit(ctx.block());
			//
			DEPNode endSyncBlock = new DEPNode();
			endSyncBlock.setLineOfCode(-1);
			endSyncBlock.setCode("end-synchronized:" + syncStmt.getLineOfCode());
			addNodeAndPreEdge(endSyncBlock);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(endSyncBlock);
			return null;
		}

		@Override
		public Void visitTryStatement(JavaParser.TryStatementContext ctx) {
			// 'try' block (catchClause+ finallyBlock? | finallyBlock)
			DEPNode tryNode = new DEPNode();
			tryNode.setLineOfCode(ctx.getStart().getLine());
			tryNode.setCode("try");
			addContextualProperty(tryNode, ctx);
			addNodeAndPreEdge(tryNode);
			//
			DEPNode endTry = new DEPNode();
			endTry.setLineOfCode(-1);
			endTry.setCode("end-try:" + tryNode.getLineOfCode());
			cfg.addVertex(endTry);
			//
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(tryNode);
			tryBlocks.push(new Block(tryNode, endTry));
			visit(ctx.block());	
			// System.out.println("top: " + preNodes.peekFirst());
			
			// popAddPreEdgeTo(endTry);
			for (DEPNode end: getTryEndNodes(tryNode)) {
				if (end.getCode().equals("end-try:" + tryNode.getLineOfCode()) || end.getCode().startsWith("throw") || end.getCode().matches("return\\W.*")) {
					continue;
				}
				cfg.addEdge(new Edge<>(end, new CFEdge(CFEdge.EPSILON), endTry));
			}
			// Now visit any available catch clauses
			if (ctx.catchClause() != null && ctx.catchClause().size() > 0) {
				// 'catch' '(' variableModifier* catchType Identifier ')' block
				DEPNode endCatch = new DEPNode();
				endCatch.setLineOfCode(-1);
				endCatch.setCode("end-catch:" + tryNode.getLineOfCode());
				cfg.addVertex(endCatch);
				for (JavaParser.CatchClauseContext cx: ctx.catchClause()) {
					// connect the try-node to all catch-nodes;
					// create a single end-catch for all catch-blocks;
					DEPNode catchNode = new DEPNode();
					catchNode.setLineOfCode(cx.getStart().getLine());
					catchNode.setCode("catch (" + cx.catchType().getText() + " " + cx.Identifier().getText() + ")");
					addContextualProperty(catchNode, cx);
					cfg.addVertex(catchNode);
					for (DEPNode node: getUncatchedNodes(tryNode)) {
						cfg.addEdge(new Edge<>(node, new CFEdge(CFEdge.EPSILON), catchNode));
					}
					//
					preEdges.push(CFEdge.EPSILON);
					preNodes.push(catchNode);
					visit(cx.block());
					popAddPreEdgeTo(endCatch);
				}
				
				// connect end-catch node to end-try,
				// and push end-try to the the stack ...
				cfg.addEdge(new Edge<>(endCatch, new CFEdge(CFEdge.EPSILON), endTry));
			}

			if (ctx.finallyBlock() != null) {
				// 'finally' block
				DEPNode finallyNode = new DEPNode();
				finallyNode.setLineOfCode(ctx.finallyBlock().getStart().getLine());
				finallyNode.setCode("finally");
				addContextualProperty(finallyNode, ctx.finallyBlock());
				cfg.addVertex(finallyNode);
				for (DEPNode end: getTryEndNodes(tryNode)) {
					cfg.addEdge(new Edge<>(end, new CFEdge(CFEdge.EPSILON), finallyNode));
				}
				//
				preEdges.push(CFEdge.EPSILON);
				preNodes.push(finallyNode);
				dontPop = false;
				visit(ctx.finallyBlock().block());
				//
				DEPNode endFinally = new DEPNode();
				endFinally.setLineOfCode(-1);
				endFinally.setCode("end-finally:" + tryNode.getLineOfCode());
				addNodeAndPreEdge(endFinally);

				preEdges.push(CFEdge.EPSILON);
				preNodes.push(endFinally);
			}
			else {
				// No finally
				preEdges.push(CFEdge.EPSILON);
				preNodes.push(endTry);
			}
			// NOTE that Java does not allow a singular try-block (without catch or finally)
			return null;
		}
		
		@Override
		public Void visitTryWithResourceStatement(JavaParser.TryWithResourceStatementContext ctx) {
			// 'try' resourceSpecification block catchClause* finallyBlock?
			// resourceSpecification :  '(' resources ';'? ')'
			// resources :  resource (';' resource)*
			// resource  :  variableModifier* classOrInterfaceType variableDeclaratorId '=' expression
			DEPNode tryNode = new DEPNode();
			tryNode.setLineOfCode(ctx.getStart().getLine());
			tryNode.setCode("try");
			addContextualProperty(tryNode, ctx);
			addNodeAndPreEdge(tryNode);
			preEdges.push(CFEdge.EPSILON);
			preNodes.push(tryNode);
			//
			// Iterate over all resources ...
			for (JavaParser.ResourceContext rsrc: ctx.resourceSpecification().resources().resource()) {
				DEPNode resource = new DEPNode();
				resource.setLineOfCode(rsrc.getStart().getLine());
				resource.setCode(getOriginalCodeText(rsrc));
				//
				addContextualProperty(resource, rsrc);
				addNodeAndPreEdge(resource);
				//
				preEdges.push(CFEdge.EPSILON);
				preNodes.push(resource);
			}
			//
			DEPNode endTry = new DEPNode();
			endTry.setLineOfCode(-1);
			endTry.setCode("end-try:" + tryNode.getLineOfCode());
			cfg.addVertex(endTry);
			//
			tryBlocks.push(new Block(tryNode, endTry));
			visit(ctx.block());
			// popAddPreEdgeTo(endTry);

			for (DEPNode end: getTryEndNodes(tryNode)) {
				if (end.getCode().equals("end-try:" + tryNode.getLineOfCode()) || end.getCode().startsWith("throw") || end.getCode().matches("return\\W.*")) {
					continue;
				}
				cfg.addEdge(new Edge<>(end, new CFEdge(CFEdge.EPSILON), endTry));
			}
			// Now visit any available catch clauses
			if (ctx.catchClause() != null && ctx.catchClause().size() > 0) {
				// 'catch' '(' variableModifier* catchType Identifier ')' block
				DEPNode endCatch = new DEPNode();
				endCatch.setLineOfCode(-1);
				endCatch.setCode("end-catch:" + tryNode.getLineOfCode());
				cfg.addVertex(endCatch);
				for (JavaParser.CatchClauseContext cx: ctx.catchClause()) {
					// connect the try-node to all catch-nodes;
					// create a single end-catch for all catch-blocks;
					DEPNode catchNode = new DEPNode();
					catchNode.setLineOfCode(cx.getStart().getLine());
					catchNode.setCode("catch (" + cx.catchType().getText() + " " + cx.Identifier().getText() + ")");
					addContextualProperty(catchNode, cx);
					cfg.addVertex(catchNode);

					for (DEPNode node: getUncatchedNodes(tryNode)) {
						cfg.addEdge(new Edge<>(node, new CFEdge(CFEdge.EPSILON), catchNode));
					}
					//
					preEdges.push(CFEdge.EPSILON);
					preNodes.push(catchNode);
					visit(cx.block());
					popAddPreEdgeTo(endCatch);
				}
				
				// connect end-catch node to end-try,
				// and push end-try to the the stack ...
				cfg.addEdge(new Edge<>(endCatch, new CFEdge(CFEdge.EPSILON), endTry));
			}

			if (ctx.finallyBlock() != null) {
				// 'finally' block
				DEPNode finallyNode = new DEPNode();
				finallyNode.setLineOfCode(ctx.finallyBlock().getStart().getLine());
				finallyNode.setCode("finally");
				addContextualProperty(finallyNode, ctx.finallyBlock());
				cfg.addVertex(finallyNode);
				for (DEPNode end: getTryEndNodes(tryNode)) {
					cfg.addEdge(new Edge<>(end, new CFEdge(CFEdge.EPSILON), finallyNode));
				}
				//
				preEdges.push(CFEdge.EPSILON);
				preNodes.push(finallyNode);
				dontPop = false;
				visit(ctx.finallyBlock().block());
				//
				DEPNode endFinally = new DEPNode();
				endFinally.setLineOfCode(-1);
				endFinally.setCode("end-finally:" + tryNode.getLineOfCode());
				addNodeAndPreEdge(endFinally);

				preEdges.push(CFEdge.EPSILON);
				preNodes.push(endFinally);
			}
			else {
				// No finally
				preEdges.push(CFEdge.EPSILON);
				preNodes.push(endTry);
			}
			return null;
		}

		@Override
		public Void visitThrowStatement(JavaParser.ThrowStatementContext ctx) {
			// 'throw' expression ';'
			DEPNode throwNode = new DEPNode();
			throwNode.setLineOfCode(ctx.getStart().getLine());
			throwNode.setCode("throw " + getOriginalCodeText(ctx.expression()));
			addContextualProperty(throwNode, ctx);
			addNodeAndPreEdge(throwNode);
			//
			// if (!tryBlocks.isEmpty()) {
			// 	Block tryBlock = tryBlocks.peek();
			// 	cfg.addEdge(new Edge<>(throwNode, new CFEdge(CFEdge.THROWS), tryBlock.end));
			// } else {
			// 	// do something when it's a throw not in a try-catch block ...
			// 	// in such a situation, the method declaration has a throws clause;
			// 	// so we should create a special node for the method-throws, 
			// 	// and create an edge from this throw-statement to that throws-node.
			// }
			dontPop = true;
			return null;
		}

		/**
		 * Add this node to the CFG and create edge from pre-node to this node.
		 */
		private void addNodeAndPreEdge(DEPNode node) {
			cfg.addVertex(node);
			popAddPreEdgeTo(node);
		}

		/**
		 * Add a new edge to the given node, by poping the edge-type of the stack.
		 */
		private void popAddPreEdgeTo(DEPNode node) {
			if (dontPop)
				dontPop = false;
			else {
				Logger.debug("\nPRE-NODES = " + preNodes.size());
				Logger.debug("PRE-EDGES = " + preEdges.size() + '\n');
				cfg.addEdge(new Edge<>(preNodes.pop(), new CFEdge(preEdges.pop()), node));
			}
			//
			for (int i = casesQueue.size(); i > 0; --i)
				cfg.addEdge(new Edge<>(casesQueue.remove(), new CFEdge(CFEdge.TRUE), node));
		}

		/**
		 * Get the original program text for the given parser-rule context.
		 * This is required for preserving whitespaces.
		 */
		private String getOriginalCodeText(ParserRuleContext ctx) {
			int start = ctx.start.getStartIndex();
			int stop = ctx.stop.getStopIndex();
			Interval interval = new Interval(start, stop);
			return ctx.start.getInputStream().getText(interval);
		}

		private Set<DEPNode> getUncatchedNodes(DEPNode tryNode) {
			Set<DEPNode> nodes = new HashSet<>();
			Deque<DEPNode> internals = new ArrayDeque<>();
			Set<DEPNode> visited = new HashSet<>();
			internals.push(tryNode);

			while (!internals.isEmpty()) {
				DEPNode cur = internals.pop();
				if (cfg.getOutDegree(cur) == 0) {
					continue;
				}
				Iterator<Edge<DEPNode, CFEdge>> iter = cfg.outgoingEdgesIterator(cur);
				while (iter.hasNext()) {
					DEPNode next = iter.next().target;
					if (visited.contains(next)) continue;
					visited.add(next);
					internals.push(next);
					boolean catched = false;
					Iterator<Edge<DEPNode, CFEdge>> nextIter = cfg.outgoingEdgesIterator(next);
					while (nextIter.hasNext()) {
						if (nextIter.next().target.getCode().startsWith("catch")) {
							catched = true;
							break;
						}
					}
					if (!catched && next.getLineOfCode() != -1) {
						nodes.add(next);
					}
				}
			}
			return nodes;
		}
		
		private Set<DEPNode> getTryEndNodes(DEPNode node) {
			Deque<DEPNode> internals = new ArrayDeque<>();
			Set<DEPNode> visited = new HashSet<>();
			Set<DEPNode> ends = new HashSet<>();
			internals.push(node);

			while (!internals.isEmpty()) {
				DEPNode cur = internals.pop();
				if (cfg.getOutDegree(cur) == 0) {
					ends.add(cur);
				}
				else {
					
					Iterator<Edge<DEPNode, CFEdge>> iter = cfg.outgoingEdgesIterator(cur);
					while (iter.hasNext()) {
						DEPNode next = iter.next().target;
						if (visited.contains(next)) continue;
						visited.add(next);
						internals.push(next);
					}
				}
			}
			return ends;
		}

		/**
		 * A simple structure for holding the start, end, and label of code blocks.
		 * These are used to handle 'break' and 'continue' statements.
		 */
		private class Block {

			public final String label;
			public final DEPNode start, end;

			Block(DEPNode start, DEPNode end, String label) {
				this.start = start;
				this.end = end;
				this.label = label;
			}

			Block(DEPNode start, DEPNode end) {
				this(start, end, "");
			}
		}
	}
}
