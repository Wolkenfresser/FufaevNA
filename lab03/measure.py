"""
Замеры времени для наивной рекурсивной функции Фибоначчи.
"""

import time
from recursion import fibonacci


def measure(n: int):
    start = time.time()
    result = fibonacci(n)
    end = time.time()
    print(f"n={n}")
    print("result =", result)
    print(f"time = {end - start:.6f} sec")


if __name__ == "__main__":
    for n in [20, 25, 30, 35]:
        measure(n)