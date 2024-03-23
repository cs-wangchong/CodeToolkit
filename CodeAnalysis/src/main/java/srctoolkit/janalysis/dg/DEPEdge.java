package srctoolkit.janalysis.dg;

public class DEPEdge {
    private Type type;
    private String label;

    public DEPEdge(Type type, String label) {
        this.type = type;
        this.label = label;
    }

    public Type getType() {
        return type;
    }

    public String getLabel() {
        return label;
    }

    public String toString() {
        return label;
    }

    public enum Type {
        CTRL ("control flow"),
        DATA ("data flow");

        private String type;

        Type(String type) {
            this.type = type;
        }

        public String toString() {
            return type;
        }
    }
}
