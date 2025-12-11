"""
Базовые замеры для двух алгоритмов ДП.
"""

import time
from dynamic_programming import fib_dp, knapsack_01
import random


def measure_fib():
    for n in [1000, 2000, 3000]:
        start = time.time()
        fib_dp(n)
        print(f"fib_dp({n}) => {time.time() - start:.6f} sec")


def measure_knapsack():
    items = [(random.randint(10, 100), random.randint(5, 20)) for _ in range(40)]
    start = time.time()
    knapsack_01(items, capacity=200)
    print(f"0-1 knapsack => {time.time() - start:.6f} sec")


if __name__ == "__main__":
    measure_fib()
    measure_knapsack()