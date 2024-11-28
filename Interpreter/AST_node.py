
# I am just implementing just an Abstract Syntax Tree(AST) this might need furthur work on the basis o need of more node types
# .
class ASTNode:
    pass

class AssignNode(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr
class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value
