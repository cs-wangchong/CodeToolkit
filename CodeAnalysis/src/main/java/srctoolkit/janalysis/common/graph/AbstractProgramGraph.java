/*** In The Name of Allah ***/
package srctoolkit.janalysis.common.graph;

import srctoolkit.janalysis.utils.Logger;

import java.io.*;

/**
 * Abstract Program Graph is the base class for all graphical program representations.
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public abstract class AbstractProgramGraph<N, E> extends Digraph<N, E> {
    
    /**
     * Default constructor.
     */
    public AbstractProgramGraph() {
        super();
    }
    
    /**
     * Copy constructor.
     */
    public AbstractProgramGraph(AbstractProgramGraph g) {
        super(g);
    }
    
	/**
	 * Export this program graph to specified file format.
     * The file will be saved in current working directory.
	 */
	public String export(String format) {
        String output = "";
        switch (format) {
            case "DOT":
                output = exportDOT();
                break;

            case "JSON":
				output = exportJSON();
             	break;
		}
        return output;
    }

    /**
	 * Export this program graph to specified file format.
     * The file will be saved in the given directory path.
	 */
	public void export(String format, String filepath) throws IOException {
		String output = export(format);
        try (FileWriter writer = new FileWriter(filepath)) {
            writer.write(output);
        } catch (UnsupportedEncodingException ex) {
			Logger.error(ex);
		}
		Logger.info("Graph exported to: " + filepath);
	}
    
    /**
     * Export this program graph to DOT format. 
     * The DOT file will be saved in current working directory. 
     * The DOT format is mainly aimed for visualization purposes.
     */
    public void exportDOT(String filepath) throws IOException {
        String dot = exportDOT();
        try (FileWriter writer = new FileWriter(filepath)) {
            writer.write(dot);
        } catch (UnsupportedEncodingException ex) {
			Logger.error(ex);
		}
		Logger.info("Graph exported to: " + filepath);
    }
    
    /**
     * Export this program graph to DOT format. 
     * The DOT file will be saved inside the given directory. 
     * The DOT format is mainly aimed for visualization purposes.
     */
    public abstract String exportDOT();

    /**
	 * Export this program graph to JSON format.
	 * The JSON file will be saved in current working directory.
	 */
    public void exportJSON(String filepath) throws IOException {
        String json = exportJSON();
        try (FileWriter writer = new FileWriter(filepath)) {
            writer.write(json);
        } catch (UnsupportedEncodingException ex) {
			Logger.error(ex);
		}
		Logger.info("Graph exported to: " + filepath);
    }
	
	/**
	 * Export this program graph to JSON format.
	 * The JSON file will be saved inside the given directory path.
	 */
	public abstract String exportJSON();
}
