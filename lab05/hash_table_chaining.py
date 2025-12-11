"""
Хеш‑таблица методом цепочек.
Уровень: 3.
"""

from hash_functions import simple_hash


class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Операция вставки
    # Средний случай: O(1)
    # Худший случай (все в одну корзину): O(n)
    def insert(self, key, value):
        index = simple_hash(key) % self.size
        bucket = self.table[index]

        # Проверка на обновление
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    # Операция поиска
    # Средний случай: O(1)
    # Худший: O(n)
    def get(self, key):
        index = simple_hash(key) % self.size
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    # Операция удаления
    # Средний случай: O(1)
    # Худший: O(n)
    def remove(self, key):
        index = simple_hash(key) % self.size
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


if __name__ == "__main__":
    ht = HashTableChaining(5)
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("c", 3)
    print(ht.get("b"))
    ht.remove("b")
    print(ht.get("b"))