import logging

logging.getLogger(__name__)

class ItemGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []
            logging.info(f"---{node} added")

    def add_edge(self, source_node, destination_node):
        if source_node in self.nodes and destination_node in self.nodes:
            self.nodes[source_node].append(destination_node)
            logging.info(f"---{source_node}-{destination_node} edge added")

    def dfs(self, start, visited=None):
        logging.info(self.nodes)
        if visited is None:
            visited = set()
        visited.add(start)
        logging.info(start)
        for neighbor in self.nodes[start]:

            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        logging.info(start)

