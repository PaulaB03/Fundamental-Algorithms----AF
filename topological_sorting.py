# Print the graph
def print_graph():
    for node in graph:
        print(node, " -> ", graph[node])


# Read the graph
def read_graph():
    global graph, in_degree, numCourses

    f = open('3.in')

    numCourses = int(f.readline())

    for line in f:
        node1, node2 = map(int, line.split())

        # Check if the nodes have been added to the graph
        if node1 not in graph:
            graph[node1] = []
            in_degree[node1] = 0
        if node2 not in graph:
            graph[node2] = []
            in_degree[node2] = 0

        # Add the edge and memorize the internal degree
        graph[node2].append(node1)
        in_degree[node1] += 1

    f.close()


# Topological sorting
def topological_sorting():
    queue, order = [], []

    # Add the nodes that have the internal degree 0 to the queue
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    while queue:
        current = queue.pop(0)
        order.append(current)

        # Subtract one from all the nodes connected to the current node
        for node in graph[current]:
            in_degree[node] -= 1

            # If a node reaches in_degree 0, add it to the queue
            if in_degree[node] == 0:
                queue.append(node)

    if len(order) == numCourses:
        return order
    else:
        return [0]


graph, in_degree, numCourses = {}, {}, 0
read_graph()
print(topological_sorting())
