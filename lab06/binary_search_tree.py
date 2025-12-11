"""
Бинарное дерево поиска (BST) — минимальный набор для оценки «3».
Реализовано:
- класс TreeNode
- класс BinarySearchTree c методами insert, search, in_order
Сложности: O(log n) в среднем, O(n) в худшем случае (вырожденное дерево).
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка
    # Средний случай: O(log n)
    # Худший случай: O(n)
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)
        # равные значения не вставляем

    # Поиск
    # Средний случай: O(log n)
    # Худший: O(n)
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # Рекурсивный обход (in-order): левый — корень — правый
    # Сложность: O(n)
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)
    print("In-order:", bst.in_order())
    print("Search 6:", bst.search(6))
    print("Search 10:", bst.search(10))