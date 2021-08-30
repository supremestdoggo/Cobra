# Cobra

Cobra is an optimizer for Python bytecode. It performs several mini-optimizations on ASTs, many of which are from [Python byte-code and micro-optimization](https://medium.com/@chipiga86/python-byte-code-and-micro-optimization-1c0acb902c9). It can be downloaded using pip (`pip install cobra-opt`) and used like so:  
Optimize a single Python file: `python3 -m cobra-opt file.py`  
Optimize a folder of Python files: `python3 -m cobra-opt -d directory/` or `python3 -m cobra-opt --directory directory/`
