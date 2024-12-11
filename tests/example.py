def add(a, b):
    """Функция для сложения двух чисел."""
    return a + b


def divide(a, b):
    """Функция для деления двух чисел."""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b
