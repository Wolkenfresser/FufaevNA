"""
Min-Heap (минимальная куча)
Уровень: 3
Операции: insert, extract
Сложность:
- insert: O(log n)
- extract: O(log n)
"""

class MinHeap:
    def __init__(self):
        self.data = []

    # Вставка элемента
    # Сложность: O(log n)
    def insert(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    # Извлечение минимума (корня)
    # Сложность: O(log n)
    def extract(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._sift_down(0)
        return root

    def _sift_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break


if __name__ == "__main__":
    h = MinHeap()
    for x in [5, 3, 8, 1, 4]:
        h.insert(x)
    print("Extracted:", h.extract())
    print("Heap state:", h.data)