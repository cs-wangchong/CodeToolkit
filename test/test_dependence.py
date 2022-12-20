from codetoolkit.dependency_analyzer import DependencyAnalyzer

if __name__ == '__main__':
    code  = open("test/Sample1.java", "r").read()
    analyzer = DependencyAnalyzer()
    cfg = analyzer.build_cfg(code)
    pdg = analyzer.build_pdg(code)
    print(cfg)
    print(pdg)

