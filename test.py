from cobra_opt import optimize

@optimize
def f(n):
    if n > 0:
        return 1 + 7
    else:
        return 1 - 7

print(f(1))