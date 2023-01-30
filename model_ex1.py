from Graph import *


def read():
    global graph

    file = open("graf.in")

    n,m = map(int, file.readline().split())

    # Add the nodes in the graph
    for i in range(n):
        graph.add_node(i+1)

    # Add the edges in the graph
    for _ in range(m):
        node1, node2 = map(int, file.readline().split())
        graph.add_edge(node1, node2)

    s = int(file.readline())
    file.close()

    return s


# DFS algorithm
def dfs(node, visited, queue):
    visited.remove(node)
    queue.append(node)

    for neighbour in graph.nodes[node].get_neighbours():
        if neighbour in visited:
            dfs(neighbour, visited, queue)


# Conex components
def conex_comp():
    global nr_cc

    visited = [node for node in graph.nodes]

    while visited:
        current = visited[0]
        cc[nr_cc] = []

        # un dfs construieste o componenta conexa
        dfs(current, visited, cc[nr_cc])
        nr_cc += 1


# DFS with distances



graph = Graph()
s = read()

# a) Numarul de muchii pe care trebuie sa il adaugam este p-1, unde p este numarul de componente conexe.
# Aflam care sunt componentele conexe si le conectam intre ele pentru a creea o singura componenta conexa.
print("a)")
visited = [node for node in graph.nodes]
nr_cc, cc = 0, {}
conex_comp()

for i in range(nr_cc-1):
    print(cc[i][0], cc[i+1][0])
    graph.add_edge(cc[i][0], cc[i+1][0])


# Facem un BFS din nodul de start pentru a afla distanta de la nodul s la toate celelate noduri
print("b)")
distance = graph.bfs(s)

# Afisam distanta maxima
print(max(distance.values()))

print(graph.edges)