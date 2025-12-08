"""
Базовые замеры времени для трех алгоритмов сортировки.
"""

import random
import time
from sorts import bubble_sort, selection_sort, insertion_sort


def measure_once(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start


def main():
    sizes = [100, 500, 1000]

    for n in sizes:
        arr = [random.randint(0, 10000) for _ in range(n)]
        print(f"\nРазмер массива: {n}")
        print("Bubble:", measure_once(bubble_sort, arr))
        print("Selection:", measure_once(selection_sort, arr))
        print("Insertion:", measure_once(insertion_sort, arr))


if __name__ == "__main__":
    main()