from AST_node import AssignNode, BinOpNode, PrintNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = 0

    def parse(self):
        # Parse individual statements (assignment or print)
        token_type, token_value = self.tokens[self.current_pos]
        if token_type == "LET":
            node = self.parse_assignment()
            self.consume("SEMI")  # Consume the semicolon
            return node
        elif token_type == "PRINT":
            node = self.parse_print()
            self.consume("SEMI")  # Consume the semicolon
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token_type}")

    def parse_assignment(self):
        # Parse 'let <ID> = <expression>'
        self.consume("LET")  # Consume 'let'
        var_name = self.consume("ID")[1]  # Get the variable name
        self.consume("ASSIGN")  # Consume '='
        expr = self.parse_expression()  # Parse the expression on the right-hand side
        return AssignNode(var_name=var_name, expr=expr)

    def parse_print(self):
        # Parse 'print(<expression>)'
        self.consume("PRINT")  # Consume 'print'
        self.consume("LPAREN")  # Consume '('
        expr = self.parse_expression()  # Parse the expression inside the parentheses
        self.consume("RPAREN")  # Ensure the parentheses are closed
        return PrintNode(expr=expr)

    def parse_expression(self):
        # Handle primary expressions: numbers, identifiers, or parentheses
        if self.tokens[self.current_pos][0] == "LPAREN":
            self.consume("LPAREN")  # Consume '('
            expr = self.parse_expression()  # Parse the sub-expression inside parentheses
            self.consume("RPAREN")  # Ensure the parentheses are closed
            return expr

        elif self.tokens[self.current_pos][0] in ("NUMBER", "ID"):
            left = self.consume(self.tokens[self.current_pos][0])  # Consume number or identifier
        else:
            raise SyntaxError(f"Expected a NUMBER, ID, or LPAREN, got {self.tokens[self.current_pos]}")

        # Handle binary operations
        while (self.current_pos < len(self.tokens) and 
               self.tokens[self.current_pos][0] in ("PLUS", "MINUS", "MUL", "DIV")):
            op = self.consume(self.tokens[self.current_pos][0])  # Consume the operator
            if self.tokens[self.current_pos][0] in ("NUMBER", "ID", "LPAREN"):
                right = self.parse_expression()  # Recursive call to parse the right operand
                left = BinOpNode(left=left[1], op=op[0], right=right)
            else:
                raise SyntaxError(f"Expected a NUMBER, ID, or LPAREN after {op}, got {self.tokens[self.current_pos]}")

        # Return the final node
        return left[1] if isinstance(left, tuple) else left

    def consume(self, expected_type):
        # Consume a token if it matches the expected type
        if self.current_pos < len(self.tokens) and self.tokens[self.current_pos][0] == expected_type:
            current_token = self.tokens[self.current_pos]
            self.current_pos += 1
            return current_token
        raise SyntaxError(f"Expected {expected_type}, got {self.tokens[self.current_pos][0]} at position {self.current_pos}")
