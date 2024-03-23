package srctoolkit.janalysis.dg.cfg;

import srctoolkit.janalysis.dg.DEPEdge;

public class CFEdge extends DEPEdge {
    public static final String EPSILON = "";
    public static final String TRUE = "True";
    public static final String FALSE = "False";
    public static final String THROWS = "Throws";
    public static final String RETURN = "Return";

    public CFEdge(String label) {
        super(Type.CTRL, label);
    }
}
