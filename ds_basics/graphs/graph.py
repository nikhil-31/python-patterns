class Node:

    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge:

    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph:

    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.node_names = []
        self.node_map = {}

    
    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self.node_map[new_node_val] = new_node
        return new_node


    def insert_edges(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None

        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node

            if from_found is None:
                from_found = Node(node_from_val)
                self.nodes.append(from_found)

            if to_found is None:
                to_found = Node(node_from_val)
                self.nodes.append(to_found)
            edge = Edge(new_edge_val, from_found, to_found)
            from_found.edges.append(edge)
            to_found.edges.append(edge)
            self.edges.append(edge)

        
    def get_edge_list(self):
        """
        This returns a list of edges
        """
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]


    def get_adjancency_list(self):
        """
        
        """
        pass

    def get_adjancency_matrix(self):
        """
        
        """
        pass


