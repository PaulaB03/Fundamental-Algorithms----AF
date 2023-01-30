from collections import defaultdict


def bfs(graph):
    length = len(graph)
    result = 0
    visited, queue = [], []

    for i in range(length):
        visited.append(set([1 << i]))
        queue.append([i, 1 << i])

    while queue:
        result = result + 1
        new_queue = []

        for node, value in queue:
            for neigbour in graph[node]:
                mid_node = (1 << neigbour) | value

                if mid_node not in visited[neigbour]:
                    if mid_node + 1 == 1 << length:
                        return result

                    visited[neigbour].add(mid_node)
                    new_queue.append([neigbour, mid_node])

        queue = new_queue

    return 0


with open("hamiltonian.in") as file:
    graph = defaultdict(list)
    i = 0

    for f in file:
        for el in map(int, f.split()):
            graph[i].append(el)
        i += 1

print(bfs(graph))