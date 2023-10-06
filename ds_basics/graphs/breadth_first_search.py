
from collections import defaultdict


class Graph:

    def __init__(self):
        # DefaultDict to store graph 
        self.graph = defaultdict(list)

    
    def add_edge(self, u, v):
        self.graph[u].append(v)