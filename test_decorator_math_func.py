import math_func
import pytest


@pytest.mark.parametrize("num1,num2,result", [
    (2, 3, 5),
    ("Hello", "World", "HelloWorld"),
    (5.4, 5.5, 10.9)
])
def test_add_decorator(num1, num2, result):
    assert math_func.add(num1, num2) == result
