#coding = utf-8

from pathlib import Path
import json
import re

import jpype

DEFAULT_JAR = str(Path(__file__).parent / "JavaAnalysis-1.0-SNAPSHOT.jar")

class CallGraphAnalyzer:
    def __init__(self, jar_path=DEFAULT_JAR):
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", f"-Djava.class.path={jar_path}")
        self.CGBuilder = jpype.JClass('codetoolkit.janalysis.cg.stat.CallGraphBuilder')
        self.pattern = re.compile(r"(\w):(.*) \((\w)\)(.*)")

    def __del__(self):
        try:
            if jpype.isJVMStarted():
                jpype.shutdownJVM()
        except Exception:
            pass

    def build_cg(self, path):
        calls = []
        for call in self.CGBuilder.build(path):
            mobj = self.pattern.match(str(call))
            calls.append({
                "caller_type": mobj.group(1),
                "caller": mobj.group(2),
                "callee_type": mobj.group(3),
                "callee": mobj.group(4),
            })
        return calls

