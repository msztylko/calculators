from sly import Lexer, Parser


def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


class RPNCalculator:

    operators = {
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
        "*": lambda x, y: y * x,
        "/": lambda x, y: y / x,
    }

    def __init__(self):
        self.stack = []

    def eval(self, expression: str):
        tokens = expression.split()
        for token in tokens:
            if is_number(token):
                self.stack.append(float(token))
            else:
                operands = self.stack.pop(), self.stack.pop()
                result = self.operators[token](*operands)
                self.stack.append(result)
        return self.stack[0]


class PNCalculator:
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    def __init__(self):
        self.operand_stack = []
        self.operator_stack = []

    def eval(self, expr):
        tokens = expr.split()
        for token in tokens:
            if is_number(token):
                if self.operand_stack:
                    operand1 = float(self.operand_stack.pop())
                    operand2 = float(token)
                    operator = self.operator_stack.pop()
                    result = self.operators[operator](operand1, operand2)
                    self.operand_stack.append(result)
                else:
                    self.operand_stack.append(token)
            else:
                self.operator_stack.append(token)
        return self.operand_stack[0]


# SLY implementation


class CalcLexer(Lexer):
    tokens = {NAME, NUMBER}
    ignore = " \t"
    literals = {"=", "+", "-", "*", "/", "(", ")"}

    # Tokens
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r"\n+")
    def newline(self, t):
        self.lineno += t.value.count("\n")

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


class PNCalcParser(Parser):
    tokens = CalcLexer.tokens

    def __init__(self):
        self.names = {}

    @_('NAME "=" expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_("expr")
    def statement(self, p):
        print(p.expr)

    @_('"+" expr expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('"-" expr expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('"*" expr expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('"/" expr expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("NAME")
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print("Undefined name '%s'" % p.NAME)
            return 0


class RPNCalcParser(Parser):
    tokens = CalcLexer.tokens

    def __init__(self):
        self.names = {}

    @_('NAME "=" expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_("expr")
    def statement(self, p):
        print(p.expr)

    @_('expr expr "+"')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr expr "-"')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr expr "*"')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr expr "/"')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("NAME")
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print("Undefined name '%s'" % p.NAME)
            return 0
