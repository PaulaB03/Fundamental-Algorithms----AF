from Graph import Graph


# Read function
def read():
    file = open("catun.in")

    global graph
    n, m, k = map(int, file.readline().split())
    tower = list(map(int, file.readline().split()))

    for i in range(m):
        n1, n2, c = map(int, file.readline().split())
        graph.add_edge(n1, n2, c)

    file.close()
    return tower


# Dijkstra algorithm
def dijkstra(start):
    visited = []
    unvisited = graph.get_nodes()
    distance = dict(zip(unvisited, [1e12 for _ in unvisited]))
    distance[start] = 0

    while len(unvisited) != 1:
        current = unvisited[0]
        for node in unvisited:
            if distance[current] > distance[node]:
                current = node

        for node in unvisited:
            if graph.are_adjacent(current, node):
                distance[node] = min(distance[node], distance[current] + graph.nodes[current][node])

        unvisited.remove(current)
        visited.append(current)

    return distance


graph = Graph()
tower = read()

dist_tower = dict(zip(graph.get_nodes(), [0 for _ in graph.get_nodes()]))
distance = dijkstra(tower[0])

for i in range(0, len(tower)):
    new_dist = dijkstra(tower[i])

    for node in graph.get_nodes():
        if distance[node] != 1e12:
            if new_dist[node] == distance[node]:
                dist_tower[node] = min(node, tower[i])
            if new_dist[node] < distance[node]:
                distance[node] = new_dist[node]
                dist_tower[node] = tower[i]


for i in range(1, graph.num_nodes+1):
    if i in tower:
        print(0, end=" ")
    else:
        print(dist_tower[i], end=" ")
