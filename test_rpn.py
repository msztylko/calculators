from rpn_calculator import RPNCalculator, PNCalculator

def test_rpn():
    expr = '2 3 +'
    calculator = RPNCalculator()
    result = calculator.eval(expr)
    assert result == 5

def test_pn():
    expr = '+ 2 3'
    calculator = PNCalculator()
    result = calculator.eval(expr)
    assert result == 5
