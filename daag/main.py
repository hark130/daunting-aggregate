from daag.database import parse_database
from daag.graph import create_graph
from daag.misc import print_exception
from daag.parseargs import parse_args


def main() -> int:
    """Entry point for DAAG.

    Returns:
        0 on success, 1 on error/Exception.
    """
    # LOCAL VARIABLES
    retval = 0      # 0 for success, 1 on error
    db = None       # Path object for the input database
    node_list = []  # List of Nodes
    graph_obj = None  # graphviz.dot.Digraph object

    try:
        db = parse_args()
        node_list = parse_database(db)
        # print(f'NODE LIST: {node_list}')  # DEBUGGING
        graph_obj = create_graph(name=db.stem.split('.')[0], node_list=node_list)
        graph_obj.view()
        # print(f'GRAPH: {graph_obj}')  # DEBUGGING
    except Exception as err:
        print_exception(err)
        retval = 1

    # DONE
    return retval
