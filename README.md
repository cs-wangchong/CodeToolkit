# Code Tooltik

This is a toolkik for processing code implemented in python.
It includes bug-fixed/re-implemented/optimized version of some existing tools like [javalang](https://github.com/c2nes/javalang), [POSSE](https://github.com/samirgupta/POSSE), [spiral](https://github.com/casics/spiral).

Based on these tools, we provide following features:
- AST parsing based on the bug-fixed javalang
- tokenization for identifier based on the optimized spiral
- POS (part-of-speech) annotation for identifier based on the re-implemented POSSE
- phrase segmentation for identifier based on the re-implemented POSSE
- abbreviation & synonym relation checking based on heuristics
- token representation learning for code (code2vec) based on FastText

