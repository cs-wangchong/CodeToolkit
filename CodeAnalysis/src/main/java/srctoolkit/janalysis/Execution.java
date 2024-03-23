/*** In The Name of Allah ***/
package srctoolkit.janalysis;

import srctoolkit.janalysis.ast.ASTBuilder;
import srctoolkit.janalysis.ast.AbstractSyntaxTree;
import srctoolkit.janalysis.dg.cfg.CFGBuilder;
import srctoolkit.janalysis.dg.cfg.ControlFlowGraph;
import srctoolkit.janalysis.dg.pdg.JavaClass;
import srctoolkit.janalysis.dg.pdg.JavaClassExtractor;
import srctoolkit.janalysis.dg.pdg.PDGBuilder;
import srctoolkit.janalysis.dg.pdg.ProgramDependenceGraph;
import srctoolkit.janalysis.utils.FileUtils;
import srctoolkit.janalysis.utils.Logger;
import srctoolkit.janalysis.utils.SystemUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * A class which holds program execution options.
 * These options determine the execution behavior of the program.
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class Execution {
	
	private final ArrayList<Analysis> analysisTypes;
	private final ArrayList<String> inputPaths;
    private boolean debugMode;
	private String outputDir;
	private Formats format;
	
	public Execution() {
        debugMode = false;
		analysisTypes = new ArrayList<>();
		inputPaths = new ArrayList<>();
		format = Formats.DOT;
		outputDir = System.getProperty("user.dir");
		if (!outputDir.endsWith(File.separator))
			outputDir += File.separator;
	}
	
	/**
	 * Enumeration of different execution options.
	 */
	public enum Analysis {
		// analysis types
		CFG			("CFG"),
		PDG			("PDG"),
		AST			("AST"),
		SRC_INFO 	("INFO");
		
		private Analysis(String str) {
			type = str;
		}
		@Override
		public String toString() {
			return type;
		}
		public final String type;
	}

	/**
	 * Enumeration of different supported output formats.
	 */
	public enum Formats {
		DOT, JSON
	}
	
	
	/*=======================================================*/
	
	
	public void addAnalysisOption(Analysis opt) {
		analysisTypes.add(opt);
	}
	
	public void addInputPath(String path) {
		inputPaths.add(path);
	}
    
    public void setDebugMode(boolean isDebug) {
        debugMode = isDebug;
    }
	
	public void setOutputFormat(Formats fmt) {
		format = fmt;
	}
	
	public boolean setOutputDirectory(String outPath) {
        if (!outPath.endsWith(File.separator))
            outPath += File.separator;
		File outDir = new File(outPath);
        outDir.mkdirs();
		if (outDir.exists()) {
			if (outDir.canWrite() && outDir.isDirectory()) {
				outputDir = outPath;
				return true;
			}
		}
		return false;
	}
	
	@Override
	public String toString() {
		StringBuilder str = new StringBuilder();
		str.append("execution config:");
		str.append("\n  Output format = ").append(format);
		str.append("\n  Output directory = ").append(outputDir);
		str.append("\n  Analysis types = ").append(Arrays.toString(analysisTypes.toArray()));
		str.append("\n  Input paths = \n");
		for (String path: inputPaths)
			str.append("        ").append(path).append('\n');
		return str.toString();
	}
	
	/**
	 * Execute the PROGEX program with the given options.
	 */
	public void execute() {
		if (inputPaths.isEmpty()) {
			Logger.info("No input path provided!\nAbort.");
			System.exit(0);
		}
		if (analysisTypes.isEmpty()) {
			Logger.info("No analysis type provided!\nAbort.");
			System.exit(0);
		}
		
		Logger.info(toString());
		
		// 1. Extract source files from input-paths, based on selected language
		String[] paths = inputPaths.toArray(new String[inputPaths.size()]);
		String[] filePaths = new String[0];
		if (paths.length > 0)
			filePaths = FileUtils.listFilesWithSuffix(paths, ".java");
		Logger.info("# " + " source files = " + filePaths.length + "\n");

		if (!outputDir.endsWith(File.separator))
			outputDir += File.separator;
		File outDirFile = new File(outputDir);
		outDirFile.mkdirs();

		// 2. For each analysis type, do the analysis and output results
		for (Analysis analysis: analysisTypes) {
			
			Logger.debug("\nMemory Status");
			Logger.debug("=============");
			Logger.debug(SystemUtils.getMemoryStats());

			switch (analysis.type) {
				//
				case "AST":
					Logger.info("===== Abstract Syntax Analysis ======");
					Logger.debug("START: " + Logger.time() + '\n');
					for (String srcFile : filePaths) {
						try {
                            AbstractSyntaxTree ast = ASTBuilder.build(srcFile);
							String outputPath = srcFile.substring(0, srcFile.indexOf('.')) + "-AST."  + format.toString().toLowerCase();
							ast.export(format.toString(), outputPath);
							if (format == Formats.DOT) {
								String pngPath = srcFile.substring(0, srcFile.indexOf('.')) + "-AST.png";
								Runtime.getRuntime().exec("dot -Tpng -o \"" + pngPath + "\" \"" + outputPath + "\"");
							}
						} catch (IOException ex) {
							Logger.error(ex);
						}
					}
					break;
				//
				case "CFG":
					Logger.info("===== Control-Flow Analysis ======");
					Logger.debug("START: " + Logger.time() + '\n');

					for (String srcFile : filePaths) {
						try {
							List<ControlFlowGraph> cfgs = CFGBuilder.build(srcFile);
							for (ControlFlowGraph cfg: cfgs) {
								String outputPath = srcFile.substring(0, srcFile.indexOf('.')) + "-CFG-" + cfg.getName().hashCode() + "." + format.toString().toLowerCase();
								cfg.export(format.toString(), outputPath);
								if (format == Formats.DOT) {
									String pngPath = srcFile.substring(0, srcFile.indexOf('.'))  + "-CFG-" + cfg.getName().hashCode() + ".png";
									Runtime.getRuntime().exec("dot -Tpng -o \"" + pngPath + "\" \"" + outputPath + "\"");
								}
							}
						} catch (IOException ex) {
							Logger.error(ex);
						}
					}
					break;
				//
				case "PDG":
					Logger.info("===== Program-Dependence Analysis =====");
					Logger.debug("START: " + Logger.time() + '\n');
					for (String srcFile: filePaths) {
						try {
							List<ProgramDependenceGraph> pdgs = PDGBuilder.build(srcFile);
							for (ProgramDependenceGraph pdg: pdgs) {
								String outputPath = srcFile.substring(0, srcFile.indexOf('.')) + "-PDG-" + pdg.getName().hashCode() + "." + format.toString().toLowerCase();
								pdg.export(format.toString(), outputPath);
								if (format == Formats.DOT) {
									String pngPath = srcFile.substring(0, srcFile.indexOf('.'))  + "-PDG-" + pdg.getName().hashCode() + ".png";
									System.out.println(pdg.getName().hashCode());
									System.out.println("dot -Tpng -o \"" + pngPath + "\" \"" + outputPath + "\"");
									Process p = Runtime.getRuntime().exec("dot -Tpng -o \"" + pngPath + "\" \"" + outputPath + "\"");
									p.waitFor();
								}
								if (debugMode) {
									pdg.printAllNodesUseDefs(Logger.Level.DEBUG);
								}
							}
						} catch (IOException | InterruptedException ex) {
							Logger.error(ex);
						}
					}

					break;
				//
				case "INFO":
					Logger.info("Code Information Analysis");
					Logger.info("=========================");
					Logger.debug("START: " + Logger.time() + '\n');
					for (String srcFile : filePaths)
						analyzeInfo(srcFile);
					break;
				//
				default:
					Logger.info("\'" + analysis.type + "\' analysis is not supported!\n");
			}
			Logger.debug("\nFINISH: " + Logger.time());
		}
		//
		Logger.debug("\nMemory Status");
		Logger.debug("=============");
		Logger.debug(SystemUtils.getMemoryStats());
	}
    
	private void analyzeInfo(String srcFilePath) {
		try {
			Logger.info("========================================\n");
			Logger.info("FILE: " + srcFilePath);
			// first extract class info
			List<JavaClass> classInfoList = JavaClassExtractor.extractInfo(srcFilePath);
			for (JavaClass classInfo : classInfoList)
				Logger.info("" + classInfo);
			// then extract imports info
			if (classInfoList.size() > 0) {
				Logger.info("- - - - - - - - - - - - - - - - - - - - -");
				String[] imports = classInfoList.get(0).IMPORTS;
				for (JavaClass importInfo : JavaClassExtractor.extractImportsInfo(imports))
					Logger.info("" + importInfo);
			}
		} catch (IOException ex) {
			Logger.error(ex);
		}
	}
}
