from enum import Enum
from collections import namedtuple

class TokenKind(Enum):
    tok_eof = -1

    # commands
    tok_def = -2
    tok_extern = -3

    # primary
    tok_identifier = -4
    tok_number = -5

Token = namedtuple('Token', 'kind value')


class Lexer:
    def __init__(self, source):
        self.source = source
        self.iterator = iter(self.source)

    def get_tok(self):
        while True:
            last_char = " "

            while last_char.isspace():
                # skip whitespace
                last_char = self.get_char()

            if last_char.isalpha():
                # identifier: [a-zA-Z][a-zA-Z0-9]*
                # TODO: global yuck
                identifier_str = last_char

                last_char = self.get_char()
                while last_char.isalnum():
                    identifier_str += last_char
                    last_char = self.get_char()

                if identifier_str == "def":
                    yield Token(kind=TokenKind.tok_def, value=identifier_str)
                elif identifier_str == "extern":
                    yield Token(kind=TokenKind.tok_extern, value=identifier_str)
                else:
                    yield Token(kind=TokenKind.tok_identifier, value=identifier_str)

            if last_char.isdigit() or last_char == ".":
                # Number: [0-9.]+
                num_str = last_char

                last_char = self.get_char()
                while last_char.isdigit() or last_char == ".":
                    num_str += last_char
                    last_char = self.get_char()
                
                num_val = float(num_str)
                yield Token(kind=TokenKind.tok_number, value=num_val)

            if last_char == '#':
                # comment until end of line
                last_char = self.get_char()
                while (last_char != '\n' and last_char != '\r'):
                    last_char = self.get_char()
            
            if last_char == '\0':
                yield Token(kind=TokenKind.tok_eof, value=None)
                break

    def get_char(self):
        try:
            return next(self.iterator)
        except StopIteration:
            # EOF character
            return '\0'

if __name__ == "__main__":
    for tok in Lexer("def hello").get_tok():
        print(tok)