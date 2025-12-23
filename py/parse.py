# expr_parser.py
import re

def tokenize(expr):
    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expr)
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected=None):
        tok = self.peek()
        if expected and tok != expected:
            raise SyntaxError(f"Expected {expected} but got {tok}")
        self.pos += 1
        return tok

    def parse_E(self):
        val = self.parse_T()
        while self.peek() in ('+', '-'):
            op = self.eat()
            right = self.parse_T()
            val = val + right if op == '+' else val - right
        return val

    def parse_T(self):
        val = self.parse_F()
        while self.peek() in ('*', '/'):
            op = self.eat()
            right = self.parse_F()
            val = val * right if op == '*' else val / right
        return val

    def parse_F(self):
        tok = self.peek()
        if tok == '(':
            self.eat('(')
            val = self.parse_E()
            self.eat(')')
            return val
        else:
            return int(self.eat())  # number

def evaluate(expr):
    tokens = tokenize(expr)
    p = Parser(tokens)
    return p.parse_E()

# User input
user_input = input("Enter an arithmetic expression: ")
print(f"{user_input} = {evaluate(user_input)}")

# tests
for e in ["2+3*4", "(1+2)*3", "10-2*3", "8/(4-2)"]:
    print(f"{e:12} = {evaluate(e)}")
