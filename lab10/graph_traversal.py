from collections import deque

# BFS: O(V + E)
def bfs(graph, start):
    visited = [False] * graph.n
    queue = deque([start])
    visited[start] = True
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph.neighbors(u):
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return order


# DFS (итеративный): O(V + E)
def dfs(graph, start):
    visited = [False] * graph.n
    stack = [start]
    order = []

    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            order.append(u)

            for v in reversed(graph.neighbors(u)):
                if not visited[v]:
                    stack.append(v)

    return order
