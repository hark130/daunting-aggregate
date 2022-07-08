"""Defines functionality to parse a DAAG database file."""
# Standard
from pathlib import Path
from typing import Dict, List, Tuple
import sys
# Third Party
# Local
from daag.constants import CLOSE_LIST_DELIM, COLOR_LIST_DELIM, Node, OPEN_LIST_DELIM


def parse_database(dbase: Path) -> Tuple[List[Node], Dict]:
    """Parse all nodes and color scheme from a database file."""
    # LOCAL VARIABLES
    lines = []       # dbase entries
    node_list = []   # List of Nodes
    color_dict = {}  # Dictionary of "status" keys and "color" values

    # READ IT
    with open(dbase, 'r', encoding=sys.getdefaultencoding()) as in_file:
        lines = [line for line in in_file.read().split('\n') if line and not line.startswith('#')]

    # NODE LIST
    node_list = _parse_db_nodes(lines)
    color_dict = _parse_db_colors(lines, node_list)

    # DONE
    return tuple((node_list, color_dict))


def _parse_db_colors(lines: List[str], node_list: List[Node], default: str = 'lightgrey') -> Dict:
    """Parses the color scheme and associates the scheme with nodes in a dictionary.

    Dictionary format is <status>:<color>.  Default color is lightgrey.

    Args:
        lines: List of lines read from the database file.
        node_list: List of Node namedtuples parsed from the database file.
        default: Optional; Default color to use.
            See: https://graphviz.org/doc/info/colors.html#x11

    Raises:
        RuntimeError: No status found in the node_list.

    Returns:
        Dictionary of status:color items.
    """
    # LOCAL VARIABLES
    status_list = []  # List of status from the node_list
    color_list = []   # List of colors found in lines.
    colors = ''       # Just the colors from the database
    scheme = {}       # Return value

    # FIND KEYS (STATUS)
    for node_entry in node_list:
        if node_entry.status and node_entry.status not in status_list:
            status_list.append(node_entry.status)
    # Sort it
    status_list.sort()

    # FIND VALUES (COLOR SCHEME)
    for line in lines:
        if line.startswith(COLOR_LIST_DELIM):
            colors = line[line.find(COLOR_LIST_DELIM) + len(COLOR_LIST_DELIM):]
            color_list = colors.strip().split(',')
            break

    # CREATE DICTIONARY
    if not status_list:
        raise RuntimeError('No statuses found in the database')
    while len(color_list) < len(status_list):
        color_list.append(default)
    scheme = dict(zip(status_list, color_list))

    # DONE
    return scheme


def _parse_db_nodes(lines: List[str]) -> List[Node]:
    """Parse all nodes from a database file.

    Does not validate the validity of dbase but validates the content.

    Args:
        lines: A list of database entries.

    Returns:
        List of Node namedtuples read from dbase on success.
    """
    # LOCAL VARIABLES
    node_list = []     # List of Nodes
    temp_node = None   # Temp Node namedtuple

    # PARSE IT
    for line in lines:
        # Ignore empty lines and the color scheme entry
        if line and not line.startswith(COLOR_LIST_DELIM):
            temp_node = _parse_node(line)
            node_list.append(temp_node)

    # DONE
    return node_list


def _parse_list(line: str) -> Tuple[str, str]:
    """Parse a potential list entry from the front of a line.

    Args:
        line: One line parsed from a DAAG database.

    Returns:
        A tuple containing the potential list entry and the remainder.
    """
    # LOCAL VARIABLES
    list_entry = ''
    remainder = ''

    # PARSE IT
    if line.startswith(OPEN_LIST_DELIM) and line.count(CLOSE_LIST_DELIM) > 0:
        list_entry = line[:line.find(']') + 1]  # Slice out the list entry
        line = line[line.find(list_entry) + len(list_entry):]  # Remove the list entry
        _, remainder = line.split(',', maxsplit=1)  # Remove the split delimiter
    else:
        list_entry, remainder = line.split(',', maxsplit=1)

    # DONE
    return tuple((list_entry, remainder))


def _parse_node(line: str) -> Node:
    """Parse a single database entry into a Node."""
    # LOCAL VARIABLES
    temp_title = ''    # Temp Node.title
    temp_comp = ''     # Temp Node.comp
    temp_type = ''     # Temp Node.type
    temp_blocked = ''  # Temp Node.blocked
    temp_blocks = ''   # Temp Node.blocks
    temp_status = ''   # Temp Node.status
    node_obj = None    # Return value

    # PARSE IT
    temp_title, temp_comp, temp_type, line = line.split(',', maxsplit=3)
    temp_blocked, line = _parse_list(line)
    temp_blocks, temp_status = _parse_list(line)
    temp_node = Node(temp_title, temp_comp, temp_type, temp_blocked, temp_blocks, temp_status)

    # DONE
    return temp_node
