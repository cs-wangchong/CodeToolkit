/*** In The Name of Allah ***/
package srctoolkit.janalysis.ast;

import srctoolkit.janalysis.common.graph.AbstractProgramGraph;
import srctoolkit.janalysis.utils.StringUtils;
import srctoolkit.janalysis.common.graph.Edge;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;

/**
 * Abstract Syntax Tree (AST).
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class AbstractSyntaxTree extends AbstractProgramGraph<ASNode, ASEdge> {
    public final ASNode root;
	
    /**
     * Construct a new empty Abstract Syntax Tree, 
     * for the given source-code file-path.
     */
	public AbstractSyntaxTree() {
		super();
        this.root = new ASNode(ASNode.Type.ROOT);
        properties.put("label", "AST");
        properties.put("type", "Abstract Syntax Tree (AST)");
        addVertex(root);
	}
    
    /**
     * Copy constructor.
     */
    public AbstractSyntaxTree(AbstractSyntaxTree ast) {
        super(ast);
        this.root = ast.root;
    }
    
    @Override
    public String exportDOT() {
        StringBuilder dot = new StringBuilder();
        dot.append("digraph AST {\n");
        dot.append("  // graph-vertices\n");
        Map<ASNode, String> nodeNames = new LinkedHashMap<>();
        int nodeCounter = 1;
        for (ASNode node : allVertices) {
            String name = "n" + nodeCounter++;
            nodeNames.put(node, name);
            StringBuilder label = new StringBuilder("  [label=\"");
            label.append(StringUtils.escape(node.toString())).append("\"];");
            dot.append("  " + name + label.toString() + "\n");
        }
        dot.append("  // graph-edges\n");
        for (Edge<ASNode, ASEdge> edge : allEdges) {
            String src = nodeNames.get(edge.source);
            String trg = nodeNames.get(edge.target);
            dot.append("  " + src + " -> " + trg + ";\n");
        }
        dot.append("  // end-of-graph\n}\n");
        return dot.toString();
    }

	
    @Override
	public String exportJSON() {
        StringBuilder json = new StringBuilder();
		
        json.append("{\n  \"directed\": true,\n");
        for (Entry<String, String> property: properties.entrySet()) {
            switch (property.getKey()) {
                case "directed":
                    continue;
                default:
                    json.append("  \"" + property.getKey() + "\": \"" + property.getValue() + "\",\n");
            }
        }
//			json.append("  \"file\": \"" + filepath + "\",\n\n");
        json.append("  \"nodes\": [\n");
        //
        Map<ASNode, Integer> nodeIDs = new LinkedHashMap<>();
        int nodeCounter = 0;
        for (ASNode node: allVertices) {
            json.append("    {\n");
            json.append("      \"id\": " + nodeCounter + ",\n");
            json.append("      \"line\": " + node.getLineOfCode() + ",\n");
            json.append("      \"type\": \"" + node.getType() + "\",\n");
            String code = node.getCode();
            code = StringUtils.isEmpty(code) ? node.getType().label : StringUtils.escape(code);
            json.append("      \"label\": \"" + code + "\",\n");
            String normalized = node.getNormalizedCode();
            normalized = StringUtils.isEmpty(normalized) ? code : StringUtils.escape(normalized);
            json.append("      \"normalized\": \"" + normalized + "\"\n");
            nodeIDs.put(node, nodeCounter);
            ++nodeCounter;
            if (nodeCounter == allVertices.size())
                json.append("    }\n");
            else
                json.append("    },\n");
        }
        //
        json.append("  ],\n\n  \"edges\": [\n");
        int edgeCounter = 0;
        for (Edge<ASNode, ASEdge> edge: allEdges) {
            json.append("    {\n");
            json.append("      \"id\": " + edgeCounter + ",\n");
            json.append("      \"source\": " + nodeIDs.get(edge.source) + ",\n");
            json.append("      \"target\": " + nodeIDs.get(edge.target) + ",\n");
            json.append("      \"label\": \"\"\n");  // TODO: should be 'edge.label'; 
            // Java-AST-Builder uses Digraph::addEdge(V, V) which is addEdge(new Edge(V, null, V))!
            // Using a null edge label can have its use-cases, but in this case we need something like
            // Digraph::addDefaultEdge(V, V) which is addEdge(V, new E(), V) using a default constructor.
            ++edgeCounter;
            if (edgeCounter == allEdges.size())
                json.append("    }\n");
            else
                json.append("    },\n");
        }
        json.append("  ]\n}\n");
		return json.toString();
    }
}
