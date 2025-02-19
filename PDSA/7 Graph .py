# Find Shortest Path Using BFS
from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))

graph = {0: [1, 2], 1: [2, 3], 2: [3], 3: []}
print(bfs_shortest_path(graph, 0, 3))  # Output: [0, 1, 3]
