from AST_node import AssignNode,BinOpNode,PrintNode

class Interpreter:
    def __init__(self):
        self.variables = {}  # Environment to store variable values

    def visit(self, node):
        if isinstance(node, AssignNode):
            # Evaluate the expression and assign it to the variable
            value = self.visit(node.expr)
            self.variables[node.var_name] = value
        elif isinstance(node, BinOpNode):
            # Evaluate both sides of the binary operation
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
            # Evaluate the expression and print the result
            print(self.visit(node.expr))
        elif isinstance(node, int):
            # Return numeric literals directly
            return node
        elif isinstance(node, str):
            # Look up variable values
            if node in self.variables:
                return self.variables[node]
            else:
                raise NameError(f"Variable '{node}' is not defined")
        else:
            raise ValueError(f"Unsupported node type: {type(node)}")
