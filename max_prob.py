from Graph import Graph
from heapq import heappop, heappush


def read():
    file = open("max_prob.in")

    global graph
    n, m = map(int, file.readline().split())

    for i in range(m):
        n1, n2, c = map(float, file.readline().split())
        graph.add_edge(int(n1), int(n2), c)

    start, finish = map(int, file.readline().split())

    file.close()
    return start, finish


# Dijkstra algorithm with min-heap
def max_prob(start, finish):
    max_heap = [(-1, start)]
    seen = set()

    while max_heap:
        cost, node = heappop(max_heap)

        # We don't need to check a node twice
        if node in seen:
            continue

        # Check if current node is finish node
        if node == finish:
            # Return the maximum distance
            return -cost

        seen.add(node)

        for neighbour in graph.nodes:
            if neighbour not in seen:
                heappush(max_heap, (cost * graph.nodes[neighbour][node], neighbour))

    # No path from start to end
    return 0.0


graph = Graph()
s, f = read()
print(max_prob(s, f))
