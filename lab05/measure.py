"""
Базовые замеры работы хеш‑таблицы.
Уровень: 3.
"""

import time
from hash_table_chaining import HashTableChaining


def measure(n=10000):
    ht = HashTableChaining(100)

    # Замер вставки
    start = time.time()
    for i in range(n):
        ht.insert(str(i), i)
    end = time.time()
    print(f"Вставка {n} элементов: {end - start:.6f} sec")

    # Замер поиска
    start = time.time()
    for i in range(n):
        ht.get(str(i))
    end = time.time()
    print(f"Поиск {n} элементов: {end - start:.6f} sec")


if __name__ == "__main__":
    measure(5000)