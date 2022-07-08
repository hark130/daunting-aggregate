"""Defines constants and data types for DAAG."""

from collections import namedtuple
from typing import Final


# Title: uniquely identifying name (e.g., DAAG-1)
# Component: major project component/epic (e.g., config, binary, test_class)
# Type: type of ticket (e.g., test, production, research)
# Blocked: tickets that block this node, AKA "blocked by" (e.g., DAAG-1, [DAAG-1, DAAG-2])
# Blocks: tickets blocked by this node (e.g., DAAG-4, [DAAG-5, DAAG-6])
# Status: current ticket status (e.g., Open, IP, Done)
Node = namedtuple('Node', ['title', 'component', 'type', 'blocked', 'blocks', 'status'])

OPEN_LIST_DELIM: Final[str] = '['           # Database entry delimiter indicating a list beginning
CLOSE_LIST_DELIM: Final[str] = ']'          # Database entry delimiter indicating a list ending
COLOR_LIST_DELIM: Final[str] = '[COLORS]:'  # Database entry delimiter indicating color scheme
