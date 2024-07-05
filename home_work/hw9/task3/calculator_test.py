from home_work.hw9.task3.page import Calculator
import pytest


@pytest.mark.parametrize("num_1, num_2, operation, expected_result", [
    (7, 8, "+", "15"),
    (6, 2, "-", "4"),
    (5, 4, "x", "20"),
    (9, 3, "÷", "3")
])
def test_calculation_result(browser, num_1, num_2, operation, expected_result):
    calc = Calculator(browser)
    calc.open()
    calc.set_delay(10)

    calc.press(num_1)
    calc.press(operation)
    calc.press(num_2)
    calc.press("=")

    assert calc.get_result() == expected_result
