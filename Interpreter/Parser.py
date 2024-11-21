from Interpreter.AST_node import AssignNode, BinOpNode, PrintNode
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = 0

    def parse(self):
        # Example parsing logic for an assignment
        token_type, token_value = self.tokens[self.current_pos]
        if token_type == "LET":
            return self.parse_assignment()
        elif token_type == "PRINT":
            return self.parse_print()
        raise SyntaxError("Unexpected token!")

    def parse_assignment(self):
        self.consume("LET")
        var_name = self.consume("ID")[1]
        self.consume("ASSIGN")
        expr = self.parse_expression()
        self.consume("SEMI")
        return AssignNode(var_name, expr)

    def parse_print(self):
        self.consume("PRINT")
        expr = self.parse_expression()
        self.consume("SEMI")
        return PrintNode(expr)

    def parse_expression(self):
        # Handle binary expressions like `a + b`
        left = self.consume("NUMBER")[1]
        if self.current_pos < len(self.tokens) and self.tokens[self.current_pos][0] in ("PLUS", "MINUS", "MUL", "DIV"):
            op = self.consume(self.tokens[self.current_pos][0])[0]
            right = self.consume("NUMBER")[1]
            return BinOpNode(left, op, right)
        return left

    def consume(self, expected_type):
        if self.tokens[self.current_pos][0] == expected_type:
            current_token = self.tokens[self.current_pos]
            self.current_pos += 1
            return current_token
        raise SyntaxError(f"Expected {expected_type}, got {self.tokens[self.current_pos][0]}")
