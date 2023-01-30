from Graph import Graph


def read_graph():
    global graph, permutation
    f = open('dfs.in')

    # Read number of nodes and edges
    n, m = map(int, f.readline().split())

    # Read the permutation
    permutation = [int(_) for _ in f.readline().split()]

    # Add edges in the graph
    for _ in range(m):
        node1, node2 = map(int, f.readline().split())
        graph.add_edge(node1, node2)

    f.close()


def check_dfs(current, next):
    visited.append(current)

    # Check if current and next have a direct edge
    if next in graph[current] and next not in visited:
        parent[next] = current

    # Else next should be a child of the nodes before
    else:
        # That means that current shouldn't have any nodes unvisited
        for node in graph[current]:
            # If there are the program stops
            if node not in visited:
                return 0
        else:
            # Search the actual parent of the node of next
            while parent[current] != -1:
                current = parent[current]
            parent[next] = current


graph = Graph()
permutation = []

read_graph()

# Useful variables
visited = []
parent = [0 for i in range(len(graph)+1)]
parent[permutation[0]] = -1

check = 1

for i in range(len(permutation)-1):
    if check_dfs(permutation[i], permutation[i+1]) == 0:
        check = 0
        break

print(check)
