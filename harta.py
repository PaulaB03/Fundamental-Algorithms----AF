from collections import defaultdict


def bfs(graph, s, t, parent):
    visited = [False] * (t + 1)
    queue = [s]
    visited[s] = True
    parent[s] = -1

    while queue:
        node = queue.pop()
        
        for neighbour in graph[node]:
            if not visited[neighbour] and capacity[node][neighbour] > 0:
                parent[neighbour] = node
                if neighbour == t:
                    return True
                queue.append(neighbour)
                visited[neighbour] = True

    return False


# Edmonds Karp Algorithm
def edmonds_karp():
    max_flow, min_flow = 0, float("inf")

    # Find an augmenting path
    while bfs(graph, start, end, parent):

        # Compute the bottleneck capacity
        u = end
        while u != start:
            tata = parent[u]
            if capacity[tata][u] < min_flow:
                min_flow = capacity[tata][u]
            u = tata

        # Update graph capacity
        u = end
        while u != start:
            tata = parent[u]
            capacity[tata][u] -= min_flow
            capacity[u][tata] += min_flow
            u = tata

        # Update max flow
        max_flow += min_flow

    return max_flow


# Read input
with open("harta.in") as file:
    n = int(file.readline())
    
    start, end = 0, n * 2 + 1
    graph, capacity = defaultdict(list), defaultdict(dict)
    parent = [None] * (end + 1)

    # Building the 2 graphs
    for i in range(1, n + 1):
        u, y = map(int, file.readline().split())
        graph[start].append(i)
        graph[i].append(start)
        capacity[start][i] = u
        capacity[i][start] = 0

        graph[n + i].append(end)
        graph[end].append(n + i)
        capacity[n + i][end] = y
        capacity[end][n + i] = 0


    for i in range(1, n + 1):
        for j in range(1, n + 1):
            capacity[i][n + j] = 0
            capacity[n + j][i] = 0
            
            if i != j:
                graph[i].append(n + j)
                graph[n + j].append(i)
                capacity[i][n + j] = 1


# Print edges
print(f"{edmonds_karp()}")  # m

for i in range(1, n + 1):
    for neighbour in graph[i]:
        if neighbour != start and capacity[i][neighbour] == 0 and neighbour != end:
            print(f"{i} {neighbour-n}")
