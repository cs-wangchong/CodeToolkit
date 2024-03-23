package srctoolkit.janalysis.cg;

import com.ibm.wala.classLoader.IClass;
import com.ibm.wala.classLoader.IMethod;
import com.ibm.wala.classLoader.Language;
import com.ibm.wala.core.util.config.AnalysisScopeReader;
import com.ibm.wala.core.util.strings.Atom;
import com.ibm.wala.ipa.callgraph.*;
import com.ibm.wala.ipa.callgraph.impl.DefaultEntrypoint;
import com.ibm.wala.ipa.callgraph.impl.ExplicitCallGraph;
import com.ibm.wala.ipa.callgraph.impl.Util;
import com.ibm.wala.ipa.cha.ClassHierarchy;
import com.ibm.wala.ipa.cha.ClassHierarchyException;
import com.ibm.wala.ipa.cha.ClassHierarchyFactory;
import com.ibm.wala.ipa.cha.IClassHierarchy;
import com.ibm.wala.types.Descriptor;
import com.ibm.wala.types.MethodReference;
import com.ibm.wala.util.collections.HashSetFactory;


import java.io.IOException;
import java.util.HashSet;

public class CallGraphTest {
    public static Iterable<Entrypoint> makePrimordialMainEntrypoints(ClassHierarchy cha) {
        final Atom mainMethod = Atom.findOrCreateAsciiAtom("main");
        final HashSet<Entrypoint> result = HashSetFactory.make();
        for (IClass klass : cha) {
            MethodReference mainRef =
                    MethodReference.findOrCreate(
                            klass.getReference(),
                            mainMethod,
                            Descriptor.findOrCreateUTF8("([Ljava/lang/String;)V"));
            IMethod m = klass.getMethod(mainRef.getSelector());
            if (m != null) {
                result.add(new DefaultEntrypoint(m, cha));
            }
        }
        return result::iterator;
    }


    public static void main(String[] args) throws IOException, CallGraphBuilderCancelException, ClassHierarchyException {
        String classPath = "/home/ubuntu/Workspace/ResOpMining/data/scan_repos/repos/alibaba#Sentinel";
        // represents code to be analyzed
        AnalysisScope scope = AnalysisScopeReader.instance.makeJavaBinaryAnalysisScope(classPath, null);


        ClassHierarchy cha = ClassHierarchyFactory.make(scope);
        Iterable<Entrypoint> entrypoints = makePrimordialMainEntrypoints(cha);

        AnalysisOptions options = new AnalysisOptions(scope, entrypoints);

        // builds call graph via pointer analysis
        CallGraphBuilder builder = Util.makeZeroCFABuilder(Language.JAVA, options, new AnalysisCacheImpl(), cha);
        CallGraph cg = builder.makeCallGraph(options, null);
        for (CGNode e: cg.getEntrypointNodes()) {
             System.out.println(cg.getSuccNodes(e));
        }
    }
}
