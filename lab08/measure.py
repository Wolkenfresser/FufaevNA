"""
Базовые замеры выполнения жадных алгоритмов.
"""

import time
import random
from greedy_algorithms import interval_scheduling, fractional_knapsack


def measure_interval(n=10000):
    intervals = [(random.randint(0, 10000), random.randint(1, 10000)) for _ in range(n)]
    # обеспечиваем start <= end
    intervals = [(min(a, b), max(a, b)) for a, b in intervals]

    start = time.time()
    interval_scheduling(intervals)
    print(f"Interval Scheduling ({n} интервалы): {time.time() - start:.6f} sec")


def measure_knapsack(n=10000):
    items = [(random.randint(1, 100), random.randint(1, 50)) for _ in range(n)]

    start = time.time()
    fractional_knapsack(items, capacity=5000)
    print(f"Fractional Knapsack ({n} предметов): {time.time() - start:.6f} sec")


if __name__ == "__main__":
    measure_interval(5000)
    measure_knapsack(5000)