/*** In The Name of Allah ***/
package srctoolkit.janalysis.dg.pdg;


import srctoolkit.janalysis.common.graph.AbstractProgramGraph;
import srctoolkit.janalysis.dg.DEPEdge;
import srctoolkit.janalysis.dg.cfg.CFEdge;
import srctoolkit.janalysis.dg.cfg.ControlFlowGraph;
import srctoolkit.janalysis.dg.DEPNode;
import srctoolkit.janalysis.utils.Logger;
import srctoolkit.janalysis.utils.StringUtils;
import srctoolkit.janalysis.common.graph.Edge;

import java.util.*;

/**
 * Data Dependence Graph.
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class ProgramDependenceGraph extends AbstractProgramGraph<DEPNode, DEPEdge> {

	private String name;
	private DEPNode entry;
	private List<DEPNode> params;
	
	public ProgramDependenceGraph(String name) {
		super();
		this.name = name;
		this.entry = null;
		this.params = new ArrayList<>();
        properties.put("label", "PDG");
        properties.put("type", "Program Dependence Graph (PDG)");
	}

	public String getName() {
		return name;
	}

	public void setEntry(DEPNode entry) {
		this.entry = entry;
	}

	public DEPNode getEntry() {
		return entry;
	}

	public void addParams(List<DEPNode> params) {
		this.params = params;
		for (DEPNode param: params) {
			addVertex(param);
		}
	}

	public List<DEPNode> getParams() {
		return params;
	}
	
	public void attachCFG(ControlFlowGraph cfg) {
		this.entry = cfg.getEntry();
		for (DEPNode param: this.params) {
			addVertex(param);
		}
		Iterator<DEPNode> ctrlNodes = cfg.allVerticesIterator();
		while(ctrlNodes.hasNext()) {
			DEPNode ctrlNode = ctrlNodes.next();
			addVertex(ctrlNode);
		}
		Iterator<Edge<DEPNode, CFEdge>> ctrlEdges = cfg.allEdgesIterator();
		while(ctrlEdges.hasNext()) {
			Edge<DEPNode, CFEdge> ctrlEdge = ctrlEdges.next();
			addEdge(new Edge<>(ctrlEdge.source, new DEPEdge(DEPEdge.Type.CTRL, ctrlEdge.label.getLabel()), ctrlEdge.target));
		}
	}

	public 	List<Edge<DEPNode, DEPEdge>> ctrlEdges() {
		List<Edge<DEPNode, DEPEdge>> ctrlEdges = new ArrayList<>();
		for (Edge<DEPNode, DEPEdge> edge: allEdges) {
			if (edge.label.getType() == DEPEdge.Type.CTRL) {
				ctrlEdges.add(edge);
			}
		}
		return ctrlEdges;
	}

	public 	List<Edge<DEPNode, DEPEdge>> dataEdges() {
		List<Edge<DEPNode, DEPEdge>> dataEdges = new ArrayList<>();
		for (Edge<DEPNode, DEPEdge> edge: allEdges) {
			if (edge.label.getType() == DEPEdge.Type.DATA) {
				dataEdges.add(edge);
			}
		}
		return dataEdges;
	}

	public List<Edge<DEPNode, DEPEdge>> outCtrlEdges(DEPNode node) {
		List<Edge<DEPNode, DEPEdge>> edges = new ArrayList<>();
		Iterator<Edge<DEPNode, DEPEdge>> outEdges = outgoingEdgesIterator(node);
		while (outEdges.hasNext()) {
			Edge<DEPNode, DEPEdge> out = outEdges.next();
			if (out.label.getType() == DEPEdge.Type.CTRL)
				edges.add(out);
		}
		return edges;
	}

	public List<Edge<DEPNode, DEPEdge>> outDataEdges(DEPNode node) {
		List<Edge<DEPNode, DEPEdge>> edges = new ArrayList<>();
		Iterator<Edge<DEPNode, DEPEdge>> outEdges = outgoingEdgesIterator(node);
		while (outEdges.hasNext()) {
			Edge<DEPNode, DEPEdge> out = outEdges.next();
			if (out.label.getType() == DEPEdge.Type.DATA)
				edges.add(out);
		}
		return edges;
	}

	
	public void printAllNodesUseDefs(Logger.Level level) {
		for (DEPNode node: allVertices) {
			Logger.log(node, level);
			Logger.log("  + USEs: " + Arrays.toString(node.getAllUSEs()), level);
			Logger.log("  + DEFs: " + Arrays.toString(node.getAllDEFs()) + "\n", level);
		}
	}

    @Override
    public String exportDOT() {
        return exportDOT(true);
    }

    /**
	 * Export this Data Dependence Subgraph (DDG) of PDG to DOT file format.
     * The 2nd parameter determines whether the attached CFG (if any) should also be exported.
	 * The DOT file will be saved inside the given directory.
	 * The DOT format is mainly aimed for visualization purposes.
	 */
    public String exportDOT(boolean ctrlEdgeLabels) {
		StringBuilder dot = new StringBuilder();

		dot.append("digraph PDG {\n");
		dot.append("  // graph-vertices\n");
		Map<DEPNode, String> nodeNames = new LinkedHashMap<>();
		int nodeCounter = 1;
		for (DEPNode node: params) {
			String name = "v" + nodeCounter++;
			nodeNames.put(node, name);
			StringBuilder label = new StringBuilder("  [label=\"");
			if (node.getLineOfCode() > 0)
				label.append(node.getLineOfCode()).append(":  ");
//				String code = node.getAbstract() != null ? node.getAbstract() : node.getCode();
			String code = node.getCode();
			label.append(StringUtils.escape(code)).append("\", shape=box, style=filled, fillcolor=orange];");
			dot.append("  " + name + label.toString() + "\n");
		}
		Set<DEPNode> paramNodes = new HashSet(params);
		for (DEPNode node: allVertices) {
			if (paramNodes.contains(node))
				continue;
			String name = "v" + nodeCounter++;
			nodeNames.put(node, name);
			StringBuilder label = new StringBuilder("  [label=\"");
			if (node.getLineOfCode() > 0)
				label.append(node.getLineOfCode()).append(":  ");
//				String code = node.getAbstract() != null ? node.getAbstract() : node.getCode();
			String code = node.getCode();
//				System.out.println(node.getAbstract());
			label.append(StringUtils.escape(code)).append("\"];");
			dot.append("  " + name + label.toString() + "\n");
		}
		dot.append("  // graph-edges\n");
		for (Edge<DEPNode, DEPEdge> edge: ctrlEdges()) {
			String src = nodeNames.get(edge.source);
			String trg = nodeNames.get(edge.target);
			if (ctrlEdgeLabels)
				dot.append("  " + src + " -> " + trg +
						"  [arrowhead=empty, color=gray, style=dashed, label=\"" + edge.label.getLabel() + "\"];\n");
			else
				dot.append("  " + src + " -> " + trg + "  [arrowhead=empty, color=gray, style=dashed];\n");
		}
		for (Edge<DEPNode, DEPEdge> edge: dataEdges()) {
			String src = nodeNames.get(edge.source);
			String trg = nodeNames.get(edge.target);
			dot.append("   " + src + " -> " + trg + "   [style=bold, label=\" " + edge.label.getLabel() + "\"];\n");
		}
		dot.append("  // end-of-graph\n}\n");
		return dot.toString();
	}

    
	@Override
	public String exportJSON() {
    	StringBuilder json = new StringBuilder();
		json.append("{\n  \"directed\": true,\n");
		json.append("  \"multigraph\": true,\n");
		for (Map.Entry<String, String> property: properties.entrySet()) {
			switch (property.getKey()) {
				case "directed":
					continue;
				default:
					json.append("  \"" + property.getKey() + "\": \"" + property.getValue() + "\",\n");
			}
		}
//			json.append("  \"file\": \"" + fileName + "\",\n\n\n");
		//
		Map<DEPNode, Integer> nodeNames = new LinkedHashMap<>();
		json.append("  \"nodes\": [\n");
		int nodeCounter = 0;
		for (DEPNode node: allVertices) {
			json.append("    {\n");
			json.append("      \"id\": " + nodeCounter + ",\n");
			json.append("      \"line\": " + node.getLineOfCode() + ",\n");
//				String code = node.getAbstract() != null ? node.getAbstract() : node.getCode();
			String code = node.getCode();
			json.append("      \"label\": \"" + StringUtils.escape(code) + "\",\n");
			json.append("      \"defs\": " + StringUtils.toJsonArray(node.getAllDEFs()) + ",\n");
			json.append("      \"uses\": " + StringUtils.toJsonArray(node.getAllUSEs()) + "\n");
			nodeNames.put(node, nodeCounter);
			++nodeCounter;
			if (nodeCounter == vertexCount())
				json.append("    }\n");
			else
				json.append("    },\n");
		}
		//
		json.append("  ],\n\n  \"edges\": [\n");
		int edgeCounter = 0;
		for (Edge<DEPNode, DEPEdge> edge: ctrlEdges()) {
			json.append("    {\n");
			json.append("      \"id\": " + edgeCounter + ",\n");
			json.append("      \"source\": " + nodeNames.get(edge.source) + ",\n");
			json.append("      \"target\": " + nodeNames.get(edge.target) + ",\n");
			json.append("      \"type\": \"Control\",\n");
			json.append("      \"label\": \"" + edge.label.getLabel() + "\"\n");
			++edgeCounter;
			if (edgeCounter == edgeCount())
				json.append("    }\n");
			else
				json.append("    },\n");
		}
		for (Edge<DEPNode, DEPEdge> edge: dataEdges()) {
			json.append("    {\n");
			json.append("      \"id\": " + edgeCounter + ",\n");
			json.append("      \"source\": " + nodeNames.get(edge.source) + ",\n");
			json.append("      \"target\": " + nodeNames.get(edge.target) + ",\n");
			json.append("      \"type\": \"Data\",\n");
			json.append("      \"label\": \"" + edge.label.getLabel() + "\"\n");
			++edgeCounter;
			if (edgeCounter == edgeCount())
				json.append("    }\n");
			else
				json.append("    },\n");
		}
		json.append("  ]\n}\n");
		return json.toString();
	}
}
