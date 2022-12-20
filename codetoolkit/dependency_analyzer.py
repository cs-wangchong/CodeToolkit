#coding = utf-8

from pathlib import Path
import json

import jpype

DEFAULT_JAR = str(Path(__file__).parent / "CodeAnalysis.jar")

class DependencyAnalyzer:
    def __init__(self, jar_path=DEFAULT_JAR):
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", f"-Djava.class.path={jar_path}")
        self.CFGBuilder = jpype.JClass('codeintelligence.codeanalysis.extractors.dependence.cfg.CFGBuilder')
        self.PDGBuilder = jpype.JClass('codeintelligence.codeanalysis.extractors.dependence.pdg.PDGBuilder')

    def __del__(self):
        if jpype.isJVMStarted():
            jpype.shutdownJVM()

    def build_cfg(self, code):
        cfgs = self.CFGBuilder.buildWithCode(code)
        return [json.loads(str(cfg.exportJSON())) for cfg in cfgs]

    def build_pdg(self, code):
        pdgs = self.PDGBuilder.buildWithCode(code)
        return [json.loads(str(pdg.exportJSON())) for pdg in pdgs]