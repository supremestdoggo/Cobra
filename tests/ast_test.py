import pytest
from cobra_opt.ast_optimizer import optimize_src
import random
from operator import add, sub, mul, truediv


def test_random():
    """Random testing of optimize_src."""
    for x in range(1000):
        op_str = random.choice(["+", "-", "*", "/"])
        op_func = {"+": add, sub: "-", "*": mul, "/": truediv}[op_str]
        first_int = random.randint(0, 255)
        second_int = random.randint(0, 255)
        unoptimized = str(first_int)+op_str+str(second_int)
        optimized = str(op_func(first_int, second_int))
        assert optimize_src(unoptimized) == optimized