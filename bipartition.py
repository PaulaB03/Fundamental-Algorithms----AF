# Print the graph
def print_graph():
    for node in graph:
        print(node, " -> ", graph[node])


# Read the graph
def read_graph():
    global graph
    f = open('bipartition.in')

    # Reads number of nodes and edges
    n, m = map(int, f.readline().split())

    # Add the nodes in the graph
    for i in range(1, n + 1):
        graph[i] = [[], '_']

    # Add the edges in the graph
    for i in range(m):
        node1, node2 = map(int, f.readline().split())

        graph[node1][0].append(node2)
        graph[node2][0].append(node1)

    f.close()


# Function that creates a list of the two colors
def color_list(graph):
    green = []
    red = []

    for node in graph:
        if graph[node][1] == 'red':
            red.append(node)
        if graph[node][1] == 'green':
            green.append(node)

    return [green, red]


# Bipartition function
def partition(graph, node):
    queue, visited = [node], [node]
    graph[node][1] = 'red'

    while queue:
        s = queue.pop(0)

        for neighbour in graph[s][0]:
            if graph[neighbour][1] == '_':
                graph[neighbour][1] = 'green' if graph[s][1] == 'red' else 'red'
            elif graph[neighbour][1] == graph[s][1]:
                return False

            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

    return color_list(graph)


graph = {}
read_graph()

print(partition(graph, 1))
