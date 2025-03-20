import logging

logging.getLogger(__name__)

class ItemGraph:
    def __init__(self, nodes):
        self.nodes = {}
        for node in nodes:
            self.add_node(node)
        for node in nodes:
            for subnode in node.items.all():
                self.add_edge(node, subnode)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, source_node, destination_node):
        if source_node in self.nodes and destination_node in self.nodes:
            self.nodes[source_node].append(destination_node)

    def __str__(self):
        return self.nodes

    def dfs(self, start, visited=None):
        logging.info(self.nodes)
        if visited is None:
            visited = set()
        visited.add(start)
        logging.info(start)
        for neighbor in self.nodes[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


    def pretty_dfs(self, start, visited=None, level=0):
        if visited is None:
            visited = set()
        visited.add(start)
        result = f"<p>{'*' + '--' * level + start.name}</p>"
        logging.info('--' * level + start.name)
        for daughter in self.nodes[start]:

            if daughter not in visited:
                result += self.pretty_dfs(daughter, visited, level + 1)

        return result