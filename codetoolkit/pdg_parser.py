#coding = utf-8

from pathlib import Path
import json

import jpype

DEFAULT_JAR = str(Path(__file__).parent / "CodeAnalysis.jar")

class PDGParser:
    def __init__(self, jar_path=DEFAULT_JAR):
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", f"-Djava.class.path={jar_path}")
        self.pdg_parser = jpype.JClass('codeintelligence.codeanalysis.Main')

    def __del__(self):
        if jpype.isJVMStarted():
            jpype.shutdownJVM()

    def parse(self, code):
        #get a instance of a class,this class has methods that you want to invoke 
        return json.loads(str(self.pdg_parser.getPDGJson(code)))