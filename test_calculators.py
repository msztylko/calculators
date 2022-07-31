import pytest

from calculators import PNCalculator, RPNCalculator


@pytest.mark.parametrize(
    "expression, result", [
                            ("2 3 +", 5), 
                            ("9 5 -", 4), 
                            ("3 4 *", 12), 
                            ("15 5 /", 3),
                            ("2 1 + 3 *", 9),
                            ("4 10 5 / +", 6),
                            ("10 132 9 3 + -11 * / * 17 + 5 +", 12)
                          ]
)
def test_rpn(expression, result):
    # expr =
    calculator = RPNCalculator()
    out = calculator.eval(expression)
    assert result == out


def test_pn():
    expr = "+ 2 3"
    calculator = PNCalculator()
    result = calculator.eval(expr)
    assert result == 5
