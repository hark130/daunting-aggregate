"""Defines DAAG package entry point.

Usage:
    python -m daag -h

Example Database:
    # Title, Component, Type, Blocked By, Blocks, Status
    DAAG-1,daag,prod,,,Closed
    DAAG-2,wheel,devops,DAAG-1,,Open
    DAAG-3,daag,prod,DAAG-1,,Open
    DAAG-4,daag,prod,DAAG-1,,Open
    DAAG-5,BUG,prod,DAAG-1,,Open
"""
# Standard
import sys
# Third Party
# Local
from daag.main import main


if __name__ == '__main__':
    sys.exit(main())
