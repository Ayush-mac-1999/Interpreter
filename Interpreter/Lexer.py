import re

class Lexer:
    def __init__(self, input_code):
        self.input_code = input_code
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        #for now I am only listing the common 
        token_specs = [
            ("NUMBER", r'\d+'),
            ("PLUS", r'\+'),
            ("MINUS", r'-'),
            ("MUL", r'\*'),
            ("DIV", r'/'),
            ("ASSIGN", r'='),
            ("SEMI", r';'),
            ("LPAREN", r'\('),
            ("RPAREN", r'\)'),
            ("WHITESPACE", r'\s+'),
            ("LET", r'let'),
            ("PRINT", r'print'),
            ("ID", r'[a-zA-Z_][a-zA-Z0-9_]*')
        ]
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
        for match in re.finditer(token_regex, self.input_code):
            kind = match.lastgroup
            value = match.group(kind)
            if kind != "WHITESPACE": # Ignore whitespace
                if kind=="NUMBER":
                    value=int(value)
                self.tokens.append((kind, value))
        return self.tokens
