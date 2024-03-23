/*** In The Name of Allah ***/
package srctoolkit.janalysis.dg.cfg;

import srctoolkit.janalysis.common.graph.AbstractProgramGraph;
import srctoolkit.janalysis.dg.DEPNode;
import srctoolkit.janalysis.utils.StringUtils;
import srctoolkit.janalysis.common.graph.Edge;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;

/**
 * Control Flow Graph (CFG).
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class ControlFlowGraph extends AbstractProgramGraph<DEPNode, CFEdge> {

	private String name;
	private DEPNode entry;

	public ControlFlowGraph(String name) {
		super();
		this.name = name;
		entry = null;
        properties.put("label", "CFG");
        properties.put("type", "Control Flow Graph (CFG)");
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

    @Override
	public String exportDOT() {
		StringBuilder dot = new StringBuilder();
		
		dot.append("digraph CFG {\n");
		dot.append("  // graph-vertices\n");
		Map<DEPNode, String> nodeNames = new LinkedHashMap<>();
		int nodeCounter = 1;
		for (DEPNode node: allVertices) {
			String name = "v" + nodeCounter++;
			nodeNames.put(node, name);
			StringBuilder label = new StringBuilder("  [label=\"");
			if (node.getLineOfCode() > 0)
				label.append(node.getLineOfCode()).append(":  ");
			label.append(StringUtils.escape(node.getCode())).append("\"];");
			dot.append("  " + name + label.toString() + "\n");
		}
		dot.append("  // graph-edges\n");
		for (Edge<DEPNode, CFEdge> edge: allEdges) {
			String src = nodeNames.get(edge.source);
			String trg = nodeNames.get(edge.target);
			if (edge.label.getLabel().equals(CFEdge.EPSILON))
				dot.append("  " + src + " -> " + trg + ";\n");
			else
				dot.append("  " + src + " -> " + trg + "  [label=\"" + edge.label.getLabel() + "\"];\n");
		}
		dot.append("  // end-of-graph\n}\n");
		return dot.toString();
	}	

    @Override
	public String exportJSON() {
		StringBuilder json = new StringBuilder();
		
		json.append("{\n  \"directed\": true,\n");
		json.append("  \"multigraph\": true,\n");
		for (Entry<String, String> property: properties.entrySet()) {
			switch (property.getKey()) {
				case "directed":
					continue;
				default:
					json.append("  \"" + property.getKey() + "\": \"" + property.getValue() + "\",\n");
			}
		}
//			json.append("  \"file\": \"" + fileName + "\",\n");
//            json.append("  \"package\": \"" + this.pkgName + "\",\n\n");
		//
		json.append("  \"nodes\": [\n");
		Map<DEPNode, Integer> nodeIDs = new LinkedHashMap<>();
		int nodeCounter = 0;
		for (DEPNode node: allVertices) {
			json.append("    {\n");
			json.append("      \"id\": " + nodeCounter + ",\n");
			json.append("      \"line\": " + node.getLineOfCode() + ",\n");
			json.append("      \"label\": \"" + StringUtils.escape(node.getCode()) + "\"\n");
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
		for (Edge<DEPNode, CFEdge> edge: allEdges) {
			json.append("    {\n");
			json.append("      \"id\": " + edgeCounter + ",\n");
			json.append("      \"source\": " + nodeIDs.get(edge.source) + ",\n");
			json.append("      \"target\": " + nodeIDs.get(edge.target) + ",\n");
			json.append("      \"label\": \"" + edge.label.getLabel() + "\"\n");
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
