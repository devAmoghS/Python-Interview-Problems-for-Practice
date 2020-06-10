# Given a graph, there are two methods to
# perform traversal on it.
# 1. Depth First Search (DFS)
# 2. Breadth First Search (BFS)

# Breadth First Search: 
# We check the adjacent nodes first and then mark them visited to explore their adjacent nodes.
# This uses a queue to keep track of the visited nodes in FIFO style
# In BFS, one vertex is selected at a time when it is visited and marked then its adjacent are visited and stored in the queue
# The goal is to get the shortest path by traversing the minimum no. of edges in the graph.
# BFS tries all the possible path at the same time and then use a tie breaking strategy to decide the best path
# It is used to search the solution in the nearest nodes
# Hence it is useful for social networks where in-depth exploration is not requirewd

# Depth First Search: 
# We check for exploration on the first single path we discovered and go deep until we encounter a dead end
# This uses a stack to keep track of the visited node and perform `backtracking` in case a dead end is met
# DFS is faster than BFS when exploration is the priority
# DFS will always find a path but that may not be the shortest path, unlike BFS

def dfs_1(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_2(graph, next, visited)
    return visited


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


# bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"]),
}

result = list(dfs_paths(graph, "A", "F"))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print(result)
