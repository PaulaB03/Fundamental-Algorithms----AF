from Graph import *


# Read function
def read(graph):
    file = open("input.in")

    n, m = map(int, file.readline().split())

    for _ in range(m):
        node1, node2 = map(int, file.readline().split())

        graph.add_edge(node1, node2)


# BFS algorithm
def bfs(graph, s):
    visited, queue = [s], [s]
    parent, distance = {s: None}, {s: 0}

    while queue:
        node = queue.pop(0)

        for neighbour in graph.nodes[node].get_neighbours():
            if neighbour not in visited:
                visited.append(neighbour)
                distance[neighbour] = distance[node] + 1
                parent[neighbour] = node
                queue.append(neighbour)

    print(parent)
    print(distance)


# DFS Algorithm
visited = set()
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph.nodes[node].get_neighbours():
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


graph = Graph(True)
read(graph)

# graph.bfs(0)
# graph.dfs(0)
# graph.topological_sorting()
graph.bipartition()