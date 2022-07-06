"""Read a DAAG database file."""
from pathlib import Path
from typing import List, Tuple
from daag.constants import CLOSE_LIST_DELIM, Node, OPEN_LIST_DELIM


def parse_database(db: Path) -> List[Node]:
    """Parse all nodes from a database file.

    Does not validate the validity of db but validates the content.
    """
    # LOCAL VARIABLES
    lines = []        # db entries
    node_list = []    # List of Nodes
    temp_node = None  # Temp Node
    temp_title = ''
    temp_comp = ''
    temp_type = '' 
    temp_blocked = ''
    temp_blocks = ''
    temp_status = ''

    # READ IT
    with open(db, 'r') as in_file:
        lines = [line for line in in_file.read().split('\n') if line and not line.startswith('#')]

    # PARSE IT
    for line in lines:
        # print(f'LINE: {line}')  # DEBUGGING
        # temp_title, temp_comp, temp_type, temp_blocked, temp_blocks, temp_status = line.split(',')
        temp_title, temp_comp, temp_type, line = line.split(',', maxsplit=3)
        # print(f'TEMP BLOCKS: {temp_blocks}')  # DEBUGGING
        # print(f'NEW LINE: {line}')  # DEBUGGING
        temp_blocked, line = _parse_list(line)
        temp_blocks, temp_status = _parse_list(line)
        temp_node = Node(temp_title, temp_comp, temp_type, temp_blocked, temp_blocks, temp_status)
        # print(f'TEMP NODE: {temp_node}')  # DEBUGGING
        node_list.append(temp_node)

    # DONE
    return node_list


def _parse_list(line: str) -> Tuple[str, str]:
    """Parse a potential list entry from the front of a line.

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
