from Graph import Graph

def read_graph():
    global graph, transpose, visited
    f = open('distance.in')

    # Read number of nodes and edges
    n, m = map(int, f.readline().split())

    # Add edges in the graph
    for _ in range(m):
        node1, node2 = map(int, f.readline().split())
        graph.add_edge(node1, node2)

    c1, c2 = map(int, f.readline().split())

    f.close()

    return c1, c2


# BFS Algorithm
def bfs(node, searched):
    visited = [node]    # List to keep track of visited nodes
    queue = [node]      # Queue list

    # Dictionary/List for the minimum distance between starting node
    distance = {_: -1 for _ in graph.graph}

    # Starting node has a distance of 0
    distance[node] = 0

    while queue:
        s = queue.pop(0)

        for neighbour in graph[s]:
            # Check if the node has not been visited
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                distance[neighbour] = distance[s] + 1

    return distance[searched]


graph = Graph()
control1, control2 = read_graph()

distance = [0 for _ in range(len(graph)+1)]

# Saves the smallest distance
for i in range(1, len(graph)+1):
    distance[i] = min(bfs(control1, i), bfs(control2, i))

print(*distance[1:])
