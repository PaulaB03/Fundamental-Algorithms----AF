class Graph:
    # Constructor
    def __init__(self):
        self.graph = {}

    # Operator []
    def __getitem__(self, node):
        return self.graph[node]

    # Len function
    def __len__(self):
        return len(self.graph)

    # Create the edges
    def add_edge(self, node1, node2):

        # Check if the nodes have been added to the graph
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        # Add the edges
        self.graph[node1].append(node2)

    # Print function
    def print_graph(self):
        for node in self.graph:
            print(f'{node} -> {self.graph[node]}')
