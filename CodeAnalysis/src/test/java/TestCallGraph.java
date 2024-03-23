
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

import srctoolkit.janalysis.cg.stat.CallGraphBuilder;

class TestCallGraph {
    public static void main(String[] args) throws IOException {
        String classPath = "/home/ubuntu/Workspace/ResOpMining/data/scan_repos/repos/aehrc#pathling";
        List<String> methodCalls = CallGraphBuilder.build(classPath);
        FileWriter fw = new FileWriter("tmp.txt");
        for (String mc : methodCalls) {
            fw.write(mc + "\n");
        }
        fw.close();
    }
}