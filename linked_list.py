"""
linked_list.py
Реализация односвязного списка (минимальный набор для оценки 3).
"""

from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional['Node'] = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_start(self, data: Any) -> None:
        """
        Вставка в начало списка.
        Сложность: O(1)
        """
        node = Node(data, self.head)
        self.head = node

    def delete_from_start(self) -> Optional[Any]:
        """
        Удаление из начала списка и возврат данных.
        Сложность: O(1)
        """
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def traversal(self) -> list:
        """
        Пройти по всем элементам и вернуть список значений.
        Сложность: O(n)
        """
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res


if __name__ == "__main__":
    # Небольшая демонстрация
    ll = LinkedList()
    ll.insert_at_start(1)
    ll.insert_at_start(2)
    ll.insert_at_start(3)
    print("Содержимое списка:", ll.traversal())
    print("Удалённый элемент:", ll.delete_from_start())
    print("После удаления:", ll.traversal())