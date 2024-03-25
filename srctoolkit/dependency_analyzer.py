#coding = utf-8

from pathlib import Path
import json

import jpype

DEFAULT_JAR = str(Path(__file__).parent / "JavaAnalysis-1.0-SNAPSHOT.jar")

class DependencyAnalyzer:
    def __init__(self, jar_path=DEFAULT_JAR):
        if not jpype.isJVMStarted():
            jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", f"-Djava.class.path={jar_path}")
        self.CFGBuilder = jpype.JClass('srctoolkit.janalysis.dg.cfg.CFGBuilder')
        self.PDGBuilder = jpype.JClass('srctoolkit.janalysis.dg.pdg.PDGBuilder')

    def __del__(self):
        try:
            if jpype.isJVMStarted():
                jpype.shutdownJVM()
        except Exception:
            pass

    def build_cfg(self, code):
        cfgs = self.CFGBuilder.buildWithCode(code)
        return [json.loads(str(cfg.exportJSON()).replace('\t', '    ')) for cfg in cfgs]

    def build_pdg(self, code):
        pdgs = self.PDGBuilder.buildWithCode(code)
        return [json.loads(str(pdg.exportJSON()).replace('\t', '    ')) for pdg in pdgs]