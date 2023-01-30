from Graph import Graph


def bfs(start, finish):
    visited = [start]
    queue = [start]

    while queue:
        current = queue.pop(0)

        if current == finish:
            return True

        for neighbour in graph[current].get_neighbours():
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return False


file = open("disjoint.in")

n, m = map(int, file.readline().split())
graph = Graph(True)

for _ in range(m):
    o, x, y = map(int, file.readline().split())

    if o == 1:
        graph.add_edge(x, y)
    else:
        if x in graph.get_nodes() and bfs(x, y):
            print("DA")
        else:
            print("NU")

file.close()
