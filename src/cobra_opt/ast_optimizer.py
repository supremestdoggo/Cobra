import ast
from operator import add, sub, mul, truediv, floordiv, mod, pow, lshift, rshift, or_, and_, matmul

# Compatability with Python 3.8
try:
    from ast import unparse
except ImportError:
    from astor.code_gen import to_source as unparse


class Optimizer(ast.NodeTransformer):
    """The Cobra optimizer for ASTs."""
    def visit_BinOp(self, node: ast.BinOp):
        if isinstance(node.left, ast.Constant) and isinstance(node.right, ast.Constant):
            operator = node.op
            left = node.left.value
            right = node.right.value
            operator_func = {"Add": add, "Sub": sub, "Mult": mul, "Div": truediv, "FloorDiv": floordiv, "Mod": mod, "Pow": pow, "LShift": lshift, "RShift": rshift, "BitOr": or_, "BitAnd": and_, "MatMult": matmul}[operator.__class__.__name__]
            return ast.Constant(value=operator_func(left, right))
        return node
    
    def visit_UnaryOp(self, node: ast.UnaryOp):
        if isinstance(node.operand, ast.Constant):
            op = node.op.__class__.__name__
            const = node.operand.value
            if op == "UAdd":
                return ast.Constant(value=+const)
            elif op == "USub":
                return ast.Constant(value=-const)
            elif op == "Not":
                return ast.Constant(value=not const)
            elif op == "Invert":
                return ast.Constant(value=~const)
        return node
    
    def visit_BoolOp(self, node: ast.BoolOp):
        for value in node.values:
            if isinstance(value, ast.Constant):
                if bool(value.value) == False:
                    return ast.Constant(value=False)
    
    def visit_If(self, node: ast.If):
        if isinstance(node.test, ast.Constant):
            if bool(node.test.value) == True:
                node.orelse = []
            else:
                node.body = node.orelse
                node.orelse = []
                return node
        elif isinstance(node.body, ast.Return):
            node = [ast.If(node.test, node.body, [])] + node.orelse
        return node


def optimize_src(source: str) -> str:
    """Optimize source code using the Cobra optimizer"""
    optimizer = Optimizer()
    tree = ast.parse(source, __file__, "exec")
    new_tree = ast.fix_missing_locations(optimizer.visit(tree))
    return unparse(new_tree)