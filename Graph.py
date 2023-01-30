class Node:
    # Constructor
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        # Node degree
        self.degree_int = 0
        self.degree_ext = 0

    # Ad a neighbour (and the cost if it exists)
    def add_neighbour(self, node, cost=0):
        self.adjacent[node] = cost
        self.set_degree_ext()
        node.set_degree_int()

    # Name of the node
    def get_id(self):
        return self.id

    # Get the nodes adjacent
    def get_neighbours(self):
        neighbours = []

        for neighbour in self.adjacent:
            neighbours.append(neighbour.get_id())

        return neighbours

    # Get the cost between the nodes
    def get_cost(self, node):
        return self.adjacent[node]

    # Check if the nodes are adjacent
    def are_adjacent(self, node):
        return node in self.get_neighbours()

    # Set internal degree
    def set_degree_int(self):
        self.degree_int += 1

    # Set external degree
    def set_degree_ext(self):
        self.degree_ext += 1

    # Get internal degree
    def get_degree_int(self):
        return self.degree_int

    # Get external degree
    def get_degree_ext(self):
        return self.degree_ext

    # [] operator // returns the cost
    def __getitem__(self, node):
        return self.adjacent[node]

    # Print node
    def __str__(self):
        return f'{self.id} connected to: {str([node.get_id() for node in self.adjacent])}'


class Graph:
    # Constructor
    def __init__(self, directed=False):
        self.nodes = {}
        self.edges = []
        self.num_nodes = 0
        self.directed = directed

    # ???
    def __iter__(self):
        return iter(self.nodes.values())

    # Creates a node object
    def add_node(self, node):
        self.num_nodes += 1
        new_node = Node(node)
        self.nodes[node] = new_node

    # Adds an edge between nodes
    def add_edge(self, node1, node2, cost=0):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)

        self.nodes[node1].add_neighbour(self.nodes[node2], cost)
        self.edges.append([node1, node2, cost])

        # If the graph is directed
        if not self.directed:
            self.nodes[node2].add_neighbour(self.nodes[node1], cost)

        if self.directed:
            self.edges.append([node2, node1, cost])

    # Get nodes list
    def get_nodes(self):
        return list(self.nodes.keys())

    # Get cost between nodes
    def get_cost(self, node1, node2):
        return self.nodes[node1][node2]

    # Check if two nodes are adjacent
    def are_adjacent(self, node1, node2):
        return self.nodes[node1].are_adjacent(node2)

    # [] operator
    def __getitem__(self, node):
        return self.nodes[node]

    # Print function
    def __str__(self):
        s = ""
        for node in self.nodes:
            s += self.nodes[node].__str__() + "\n"

        return s

    # BFS algorithm
    def bfs(self, s):
        visited, queue = [s], [s]
        parent, distance = {s: None}, {s: 0}

        while queue:
            node = queue.pop(0)

            for neighbour in self.nodes[node].get_neighbours():
                if neighbour not in visited:
                    visited.append(neighbour)
                    distance[neighbour] = distance[node] + 1
                    parent[neighbour] = node
                    queue.append(neighbour)

        # print(parent)
        # print(distance)
        return distance

    # DFS algorithm
    # A function used by DFS
    def dfs_util(self, node, visited):
        # Mark the current node as visited and print it
        visited.add(node)
        print(node, end=" ")

        # Recur for all nodes adjacent to current node
        for neighbour in self.nodes[node].get_neighbours():
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    # DFS function to do the traversal
    def dfs(self, node):
        # Create a set to store visited nodes
        visited = set()


        # Call the recursive function to print DFS traversal
        self.dfs_util(node, visited)
        print("\n")

    # Topological sorting
    def topological_sorting(self):
        queue, order = [], []

        # Add the nodes that have the internal degree 0 to the queue
        for node in self.nodes:
            if self.nodes[node].get_degree_int() == 0:
                queue.append(node)

        while queue:
            current = queue.pop(0)
            order.append(current)

            # Subtract one from all the nodes connected to the current node
            for node in self.nodes[current].get_neighbours():
                self.nodes[node].degree_int -= 1

                # If a node reaches internal degree 0, add it to the queue
                if self.nodes[node].get_degree_int() == 0:
                    queue.append(node)

        print(order)

    # Bipartition
    def bipartition(self):
        visited = self.get_nodes()
        color = {node: None for node in visited}

        while visited:
            current = visited.pop(0)
            if color[current] is None:
                color[current] = 'red'

            for neighbour in self.nodes[current].get_neighbours():
                if color[neighbour] is None:
                    color[neighbour] = 'green' if color[current] == 'red' else 'red'
                elif color[neighbour] == color[current]:
                    print("The graph isn't bipartite")
                    return 0

        print(color)
