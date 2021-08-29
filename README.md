# Cobra

Cobra is an optimizer for Python bytecode. It performs several mini-optimizations on ASTs, many of which are from [Python byte-code and micro-optimization](https://medium.com/@chipiga86/python-byte-code-and-micro-optimization-1c0acb902c9). It can be downloaded using pip (`pip install cobra-opt`) and used like so:

```py
from cobra_opt import optimize

@optimize
def f(n):
    if n > 0:
        return 1 + 7
    else:
        return 1 - 7
```

This will make `f` into  

```py
def f(n):
    if n > 0:
        return 8
    return -6
```
