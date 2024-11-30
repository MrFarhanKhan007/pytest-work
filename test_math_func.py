import math_func


def test_math_func_add():
    assert math_func.add(2, 2) == 4
    assert math_func.add(4,4) == 8
    assert math_func.add(5, 5) == 10

def test_math_func_mul():
    assert math_func.multiply(3,3) == 9
    assert math_func.multiply(4,4) ==16
    assert math_func.multiply(5,5) == 25
