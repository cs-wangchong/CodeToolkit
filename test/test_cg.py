from codetoolkit.call_graph_analyzer import CallGraphAnalyzer

if __name__ == '__main__':
    analyzer = CallGraphAnalyzer()
    calls = analyzer.build_cg("/home/ubuntu/Workspace/ResOpMining/data/scan_repos/repos/aehrc#pathling")
    print(calls)

    