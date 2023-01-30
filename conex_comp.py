from DirectedGraph import Graph


# Read function
def read_graph():
    global graph, transpose, visited
    f = open('ctc.in')

    # Read number of nodes and edges
    n, m = map(int, f.readline().split())

    # Add edges in the graph
    for _ in range(m):
        node1, node2 = map(int, f.readline().split())
        graph.add_edge(node1, node2)
        transpose.add_edge(node2, node1)

        if node1 not in visited:
            visited[node1] = 0
        if node2 not in visited:
            visited[node2] = 0

    f.close()


# DFS for the initial graph
def dfsp(node):
    visited[node] = 1

    for neighbour in graph.graph[node]:
        if visited[neighbour] == 0:
            dfsp(neighbour)

    queue.append(node)


# DFS for the transposed graph
def dfsm(node):
    visited[node] = 2

    # Add the node in current ctc
    try:
        ctc[nr_ctc].append(node)
    except KeyError:
        ctc[nr_ctc] = [node]

    for neighbour in transpose.graph[node]:
        if visited[neighbour] == 1:
            dfsm(neighbour)


def solve():
    global nr_ctc

    # Mark the node in the graph
    for node in graph.graph:
        if visited[node] == 0:
            dfsp(node)

    # For every node in the queue
    while queue:
        current = queue.pop()

        # Mark the node in the transposed graph
        if visited[current] == 1:
            nr_ctc += 1
            dfsm(current)


visited, ctc, queue = {}, {}, []
nr_ctc = 0
graph = Graph()
transpose = Graph()

read_graph()
solve()

print(nr_ctc)
for _ in ctc:
    print(ctc[_])
