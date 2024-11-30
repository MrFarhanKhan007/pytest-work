import math_func
import pytest


# @pytest.mark.number
# @pytest.mark.skip(reason="")/skipif(condition,reason="")
def test_add_integers():
    assert math_func.add(2, 2) == 4
    assert math_func.add(4, 4) == 8
    assert math_func.add(5, 5) == 10


# @pytest.mark.number
def test_mul_integer():
    assert math_func.multiply(3, 3) == 9
    assert math_func.multiply(4, 4) == 16
    assert math_func.multiply(5, 5) == 25


# @pytest.mark.string
def test_add_strings():
    result = math_func.add("Hello", "World")
    assert result == "HelloWorld"
    assert type(result) is str
    assert "heldio" not in result


# @pytest.mark.string
def test_mul_strings():
    assert math_func.multiply("Hello ", 3) == "Hello Hello Hello "
    result = math_func.multiply("Hello", 1)
    assert result == "Hello"
    assert type(result) is str
    assert "Hello" in result
