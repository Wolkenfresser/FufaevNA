class AdjacencyMatrixGraph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # неориентированный граф

    # Проверка ребра: O(1)
    def has_edge(self, u, v):
        return self.matrix[u][v] == 1


class AdjacencyListGraph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    # Добавление ребра: O(1)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # неориентированный граф

    # Получение соседей: O(k), где k — число соседей
    def neighbors(self, u):
        return self.graph[u]
