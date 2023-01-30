from Graph import Graph


def read(file, graph):
    n, m = map(int, file.readline().split())
    v = list(map(int, file.readline().split()))

    for i in range(m):
        n1, n2 = map(int, file.readline().split())
        graph.add_edge(n1, n2)

    return v


def dfs(visited, graph, node):
    global sum, v
    if node not in visited:
        sum += v[node-1]
        visited.add(node)
        for neighbour in graph.nodes[node].get_neighbours():
            dfs(visited, graph, neighbour)


file = open("easygraph.in")
t = int(file.readline())

for i in range(t):
    graph = Graph(True)
    v = read(file, graph)
    maxi = 0
    for node in range(1, graph.num_nodes+1):
        sum = 0
        visited = set()
        dfs(visited, graph, node)
        maxi = max(maxi, sum)

    print(maxi)

file.close()
