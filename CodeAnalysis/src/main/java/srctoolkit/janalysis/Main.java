/*** In The Name of Allah ***/
package srctoolkit.janalysis;

import srctoolkit.janalysis.utils.Logger;

import java.io.File;
import java.io.IOException;

/**
 * The executions starting point.
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class Main {

	/**
	 * Parse command line arguments.
	 */
	public static Execution parse(String[] args) {
		Execution exec = new Execution();
		for (int i = 0; i < args.length; ++i) {
			// options can start with either '-' or '--'
			if (args[i].startsWith("-")) {
				if (args[i].length() > 3) {
					String opt = args[i].substring(1).toLowerCase();
					if (args[i].startsWith("--"))
						opt = args[i].substring(2).toLowerCase();
					// Now process the value of opt
					switch (opt) {
						case "ast":
							exec.addAnalysisOption(Execution.Analysis.AST);
							break;
						//
						case "cfg":
							exec.addAnalysisOption(Execution.Analysis.CFG);
							break;
						//
						case "pdg":
							exec.addAnalysisOption(Execution.Analysis.PDG);
							break;
						case "info":
							exec.addAnalysisOption(Execution.Analysis.SRC_INFO);
							break;
						//
						case "help":
							printHelp(null);
							break;
						//
						case "outdir":
							if (i < args.length - 1) {
								++i;
								if (!exec.setOutputDirectory(args[i])) {
									printHelp("Output directory is not valid!");
									System.exit(1);
								}
							} else {
								printHelp("Output directory not specified!");
								System.exit(1);
							}
							break;
						//
						case "format":
							if (i < args.length - 1) {
								++i;
								switch (args[i].toLowerCase()) {
									case "dot":
										exec.setOutputFormat(Execution.Formats.DOT);
										break;
									case "json":
										exec.setOutputFormat(Execution.Formats.JSON);
										break;
									default:
										printHelp("Unknown output format: " + args[i]);
										System.exit(1);
								}
							} else {
								printHelp("Format not specified!");
								System.exit(1);
							}
							break;
						case "debug":
							exec.setDebugMode(true);
							Logger.setActiveLevel(Logger.Level.DEBUG);
							break;
						//
						case "timetags":
							Logger.setTimeTagEnabled(true);
							break;
						//
						default:
							printHelp("Unknown Option: " + args[i]);
							System.exit(1);
					}
				} else {
					printHelp("Invalid Option: " + args[i]);
					System.exit(1);
				}
			} else {
				// any argument that does not start with a '-' is considered an input file path
				File input = new File(args[i]);
				if (input.exists())
					exec.addInputPath(args[i]);
				else
					Logger.warn("WARNING -- Ignoring non-existant input path: " + args[i]);
			}
		}
		return exec;
	}

	/**
	 * Parse code to pdg with format of JSON
	 * @return	a string with json
	 */
	public static Execution parse(){
		Execution exec = new Execution();
		exec.setOutputFormat(Execution.Formats.JSON);
		return exec;
	}

	/**
	 * Prints the usage guide for the program.
	 * If an error message is given, the message is also printed to the output.
	 */
	public static void printHelp(String errMsg) {
		if (errMsg != null && !errMsg.isEmpty())
			Logger.error("ERROR -- " + errMsg + '\n');

		String[] help = {
				"USAGE:\n\n   java -jar PROGEX.jar [-OPTIONS...] /path/to/program/src\n",
				"OPTIONS:\n",
				"   -help      Print this help message",
				"   -outdir    Specify path of output directory",
				"   -format    Specify output format; either 'DOT', or 'JSON'",
				"   -ast       Perform AST (Abstract Syntax Tree) analysis",
				"   -cfg       Perfomt CFG (Control Flow Graph) analysis",
				"   -info      Analyze and extract detailed information about program source code",
				"   -pdg       Perform PDG (Program Dependence Graph) analysis\n",
				"   -debug     Enable more detailed logs (only for debugging)",
				"   -timetags  Enable time-tags and labels for logs (only for debugging)\n",
				"DEFAULTS:\n",
				"   - If not specified, the default output directory is the current working directory.",
				"   - If not specified, the default output format is DOT.",
				"   - There is no default value for analysis type.",
				"   - There is no default value for input directory path.\n",
				"NOTES:\n",
				"   - The important pre-assumption for analyzing any source code is that the ",
				"     program is valid according to the grammar of that language. Analyzing ",
				"     invalid programs has undefined results; most probably the program will ",
				"     crash!\n",
				"   - Analyzing large programs requires high volumes of system memory, so ",
				"     it is necessary to increase the maximum available memory to PROGEX.\n",
				"     In the example below, the -Xmx option of the JVM is used to provide PROGEX ",
				"     with 5 giga-bytes of system memory; which is required for the PDG analysis ",
				"     of very large programs (i.e. about one million LoC). Needless to say, this ",
				"     is possible on a computer with at least 8 giga-bytes of RAM:\n",
				"        java -Xmx5G -jar PROGEX.jar -pdg ...\n",
		};

		for (String line: help)
			Logger.info(line);
	}

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
    	//parse Java file in path
    	args = new String[]{"-cfg", "-format", "dot", "-outdir", "test_pdg", "-timetags", "test_pdg"};
		Logger.init();
		Logger.setEchoToStdOut(true);
		Logger.setTimeTagEnabled(false);
		Logger.setActiveLevel(Logger.Level.INFO);
		parse(args).execute();
	}
}
