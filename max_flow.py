# Read function
def read():
    global graph
    file = open("maxflow.in")

    n, m = map(int, file.readline().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        n1, n2, c = map(int, file.readline().split())
        graph[n1 - 1][n2 - 1] = c

    file.close()
    return n-1


# BFS Algorithm
def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for i, j in enumerate(graph[u]):
            if not visited[i] and j > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = u

                if i == t:
                    return True

    return False


# Ford Fulkerson Algorithm
def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    # Find an augmenting path
    while bfs(graph, source, sink, parent):
        path_flow, s = float("Inf"), sink

        # Compute the bottleneck capacity
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Update max flow
        max_flow += path_flow

        # Update graph capacity
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


graph = []
sink, source = read(), 0

print(ford_fulkerson(graph, source, sink))
