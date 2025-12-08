"""
Базовые рекурсивные функции.
Уровень: 3.
"""

# Факториал n!
# Сложность: O(n), глубина рекурсии = n

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Наивное вычисление n-го числа Фибоначчи
# Сложность: O(2^n), глубина рекурсии = n

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Быстрое возведение в степень (рекурсия деления степени пополам)
# Сложность: O(log n), глубина рекурсии = log n

def fast_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_pow(a, n // 2)
        return half * half
    else:
        return a * fast_pow(a, n - 1)


if __name__ == "__main__":
    print("factorial(5) =", factorial(5))
    print("fibonacci(10) =", fibonacci(10))
    print("fast_pow(2, 10) =", fast_pow(2, 10))