from Interpreter.AST_node import AssignNode, BinOpNode, PrintNode


class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        if isinstance(node, AssignNode):
            value = self.visit(node.expr)
            self.variables[node.var_name] = value
        elif isinstance(node, BinOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op == "PLUS":
                return left + right
            elif node.op == "MINUS":
                return left - right
            elif node.op == "MUL":
                return left * right
            elif node.op == "DIV":
                return left / right
        elif isinstance(node, PrintNode):
            print(self.visit(node.expr))
        elif isinstance(node, int) or isinstance(node, str):
            return self.variables.get(node, node)
        else:
            raise ValueError("Unsupported node type")
