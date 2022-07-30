def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

operators = {'+': lambda x,y: x + y}

class RPNCalculator:

    def __init__(self):
        self.stack = []
        
    def eval(self, expression: str):
        tokens = expression.split()
        for token in tokens:
            if is_number(token):
                self.stack.append(float(token))
            else:
                operands = self.stack.pop(), self.stack.pop()
                print(*operands)
                result = operators[token](*operands)
                self.stack.append(result)
        return self.stack[0]

class PNCalculator:
    
    def __init__(self):
        self.operand_stack = []
        self.operator_stack = []

    def eval(self, expr):
        tokens = expr.split()
        for token in tokens:
            if is_number(token):
                if operand_ready:
                    operand1 = float(token)
                    operand2 = float(self.operand_stack.pop())
                    operator = self.operator_stack.pop()
                    result = operators[operator](operand1, operand2)
                    self.operand_stack.append(result)
                else:
                    self.operand_stack.append(token)
                    operand_ready = True
            else:
                self.operator_stack.append(token)
                operand_ready = False
        return self.operand_stack[0]
