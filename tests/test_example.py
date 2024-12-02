import pytest

from tests.example import add, divide


# Тест для функции сложения
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


# Параметризованный тест для функции сложения
@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)]  # Тест 1  # Тест 2  # Тест 3
)
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected
