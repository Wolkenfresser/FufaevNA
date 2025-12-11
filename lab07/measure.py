"""
Базовые замеры производительности кучи.
Уровень: 3.
"""

import time
import random
from heap import MinHeap


def measure(n=10000):
    h = MinHeap()
    values = [random.randint(0, 100000) for _ in range(n)]

    # Вставка
    start = time.time()
    for v in values:
        h.insert(v)
    print(f"Вставка {n} элементов: {time.time() - start:.6f} sec")

    # Извлечение
    start = time.time()
    for _ in range(n):
        h.extract()
    print(f"Извлечение {n} элементов: {time.time() - start:.6f} sec")


if __name__ == "__main__":
    measure(5000)