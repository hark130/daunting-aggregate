# Standard
from typing import List
import os
# Third Party
import graphviz
# Local
from daag.constants import CLOSE_LIST_DELIM, Node, OPEN_LIST_DELIM


def create_graph(name: str, node_list: List[Node], engine: str = 'dot',
                 graph_fmt: str = 'png') -> graphviz.Digraph:
    """Create a hospital-based Digraph using graphviz.

    Args:
        name: Name of the graph, which is also used to prepend the filename.
        node_list: List of Nodes to add edges.
        engine: Optional; Digraph build engine: [dot], neato, sfdp, fdp
        graph_fmt: Optional; File format for Digraph: [png], pdf

    Returns:
        Directed graph, complete with node edges.

    Raises:
        TypeError: Bad data type passed in.
    """
    # LOCAL VARIABLES
    graph_obj = None   # graphviz Digraph

    # INPUT VALIDATION
    # TO DO: DON'T DO NOW...

    # CREATE GRAPH
    graph_obj = _create_graph(name=name, engine=engine, graph_fmt=graph_fmt)

    # ADD NODES/EDGES
    graph_obj = _add_edges(graph=graph_obj, node_list=node_list)

    # DONE
    return graph_obj


def _add_edge(graph: graphviz.Digraph, edges: tuple) -> graphviz.Digraph:
    """Adds edges to graph.

    WARNING: Does not validate input!
    """
    # LOCAL VARIABLES
    temp_lead_edge = edges[0]   # We might need to modify the leading edge
    temp_trail_edge = edges[1]  # We might need to modify the trailing edge

    # ADD EDGE
    graph.edge(temp_lead_edge, temp_trail_edge)

    # DONE
    return graph


def _add_edges(graph: graphviz.Digraph, node_list: List[Node]) -> graphviz.Digraph:
    """Add edges for each Node in node_list."""
    # LOCAL VARIABLES
    temp_str = ''  # Temp string

    # ADD EDGES
    for node_entry in node_list:
        # Blocked By
        if node_entry.blocked:
            if node_entry.blocked.startswith(OPEN_LIST_DELIM) and node_entry.blocked.endswith(CLOSE_LIST_DELIM):
                temp_str = node_entry.blocked[node_entry.blocked.find(OPEN_LIST_DELIM) \
                           + len(OPEN_LIST_DELIM):node_entry.blocked.find(CLOSE_LIST_DELIM)]
                for blocked in temp_str.split(','):
                    graph = _add_edge(graph, tuple((blocked, node_entry.title)))
            else:
                graph = _add_edge(graph, tuple((node_entry.blocked, node_entry.title)))
        # Blocks
        if node_entry.blocks:
            if node_entry.blocks.startswith(OPEN_LIST_DELIM) and node_entry.blocks.endswith(CLOSE_LIST_DELIM):
                temp_str = node_entry.blocks[node_entry.blocks.find(OPEN_LIST_DELIM) \
                           + len(OPEN_LIST_DELIM):node_entry.blocks.find(CLOSE_LIST_DELIM)]
                for blocks in temp_str.split(','):
                    graph = _add_edge(graph, tuple((node_entry.title, blocks)))
            else:
                graph = _add_edge(graph, tuple((node_entry.title, node_entry.blocks)))

    # DONE
    return graph


def _create_graph(name: str, engine: str, graph_fmt: str) -> graphviz.Digraph:
    """Create a Digraph, sans edges, using graphviz.

    Does not validate input.

    Args:
        name: Name of the graph, which is also used to prepend the filename.
        engine: Digraph build engine: dot, neato, sfdp, fdp
        graph_fmt: File format for Digraph: png, pdf

    Returns:
        Directed graph, without edges.
    """
    # LOCAL VARIABLES
    graph_obj = None                  # graphviz Digraph
    filename = name + f' ({engine})'  # Filename to save the graph

    # DO IT
    # Instantiate the object
    graph_obj = graphviz.Digraph(name=name, filename=os.path.join(os.getcwd(), filename),
                                 engine=engine, format=graph_fmt)

    # DONE
    return graph_obj
