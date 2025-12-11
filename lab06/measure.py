"""
Базовые замеры времени поиска в BST
"""

import random
import time
from binary_search_tree import BinarySearchTree


def build_bst(values):
    bst = BinarySearchTree()
    for v in values:
        bst.insert(v)
    return bst


def measure():
    # Сбалансированное дерево — случайный порядок
    values_random = [random.randint(0, 100000) for _ in range(5000)]
    bst_random = build_bst(values_random)

    # Вырожденное дерево — отсортированный массив
    values_sorted = list(range(5000))
    bst_sorted = build_bst(values_sorted)

    # Замер поиска
    to_find = [random.randint(0, 100000) for _ in range(1000)]

    print("Сбалансированное дерево:")
    start = time.time()
    for x in to_find:
        bst_random.search(x)
    print(f"Поиск 1000 элементов: {time.time() - start:.6f} sec")

    print("\nВырожденное дерево:")
    start = time.time()
    for x in to_find:
        bst_sorted.search(x)
    print(f"Поиск 1000 элементов: {time.time() - start:.6f} sec")


if __name__ == "__main__":
    measure()