from .choices import Operation
import logging


logging.getLogger(__name__)

def build_graph_with_attributes(graph, start, visited=None, attributes=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for child in graph.nodes[start]:
        if child not in visited:
            if attributes:
                attribute_for_this_item = attributes.filter(attribute_for=child).first()
                if attribute_for_this_item:
                    if attribute_for_this_item.operation == Operation.EXCLUDE:
                        graph.nodes.pop(child)
                        graph.nodes[start].remove(child)
                else:
                    graph = build_graph_with_attributes(graph, child, visited, attributes)

    return graph

def build_tree(graph, node, attributes=None):
    attribute = None
    if attributes:
        attribute_for_this_item = attributes.filter(attribute_for=node).first()
        logging.info(f"------attribute_for_this_item: {attribute_for_this_item}")
        if attribute_for_this_item:
            if attribute_for_this_item.operation == Operation.INCLUDE:
                attribute = "INCLUDE"
            elif attribute_for_this_item.operation == Operation.RECOMMEND:
                attribute = "RECOMMEND"
            else:
                graph.nodes.pop(node)
                graph.nodes[node].remove(node)

    return {
        "name": node.name,
        "attribute": attribute,
        "children": [build_tree(graph, child, attributes) for child in graph.nodes[node]]
    }