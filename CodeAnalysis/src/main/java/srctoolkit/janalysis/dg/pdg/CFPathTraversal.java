/*** In The Name of Allah ***/
package srctoolkit.janalysis.dg.pdg;


import srctoolkit.janalysis.dg.DEPEdge;
import srctoolkit.janalysis.dg.DEPNode;
import srctoolkit.janalysis.common.graph.Edge;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

/**
 * Control-Flow Path Traversal.
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class CFPathTraversal implements Iterator {
	
	private final DEPNode start;
	private final ProgramDependenceGraph pdg;
	private final Deque<Edge<DEPNode, DEPEdge>> paths;
	
	private DEPNode current;
	private boolean continueNextPath;
	private Edge<DEPNode, DEPEdge> nextEdge;
	
	public CFPathTraversal(ProgramDependenceGraph pdg, DEPNode startNode) {
		this.pdg = pdg;
		start = startNode;
		paths = new ArrayDeque<>();
		continueNextPath = false;
		current = null;
		nextEdge = null;
	}
	
	private DEPNode start() {
		nextEdge = null;  // new CFEdge(CFEdge.Type.EPSILON);
		current = start;
		return current;
	}
	
    @Override
	public boolean hasNext() {
		return current == null || (!paths.isEmpty()) || 
				(pdg.outCtrlEdges(current).size() > 0 && !continueNextPath);
	}
	
    @Override
	public DEPNode next() {
		if (current == null)
			return start();
		//
		if (!continueNextPath) {
			for (Edge<DEPNode, DEPEdge> out : pdg.outCtrlEdges(current)) {
				paths.push(out);
            }
        }
		continueNextPath = false;
		//
		if (paths.isEmpty())
			return null;
		nextEdge = paths.pop();
		current = nextEdge.target;
		return current;
	}
	
	public void continueNextPath() {
		continueNextPath = true;
	}
}
