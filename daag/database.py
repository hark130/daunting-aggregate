"""Defines functionality to parse a DAAG database file."""
# Standard
from pathlib import Path
from typing import List, Tuple
import sys
# Third Party
# Local
from daag.constants import CLOSE_LIST_DELIM, Node, OPEN_LIST_DELIM


def parse_database(dbase: Path) -> List[Node]:
    """Parse all nodes from a database file.

    Does not validate the validity of dbase but validates the content.

    Args:
        dbase: Path object of the DAAG database to parse.

    Returns:
        List of Node namedtuples read from dbase on success.
    """
    # LOCAL VARIABLES
    lines = []         # dbase entries
    node_list = []     # List of Nodes
    temp_node = None   # Temp Node namedtuple
    temp_title = ''    # Temp Node.title
    temp_comp = ''     # Temp Node.comp
    temp_type = ''     # Temp Node.type
    temp_blocked = ''  # Temp Node.blocked
    temp_blocks = ''   # Temp Node.blocks
    temp_status = ''   # Temp Node.status

    # READ IT
    with open(dbase, 'r', encoding=sys.getdefaultencoding()) as in_file:
        lines = [line for line in in_file.read().split('\n') if line and not line.startswith('#')]

    # PARSE IT
    for line in lines:
        temp_title, temp_comp, temp_type, line = line.split(',', maxsplit=3)
        temp_blocked, line = _parse_list(line)
        temp_blocks, temp_status = _parse_list(line)
        temp_node = Node(temp_title, temp_comp, temp_type, temp_blocked, temp_blocks, temp_status)
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
