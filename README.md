# daunting-aggregate

Creates a directed graph based on an ingested database of backlog items.  Written in Python 3.10.  Nodes are color-coded by status with the `[COLORS]` scheme.

## Usage

`python -m daag -h`

## Database Example

```
# Title, Component, Type, Blocked By, Blocks, Status
DAAG-1,daag,prod,,,Closed
DAAG-2,wheel,devops,DAAG-1,,Open
DAAG-3,daag,prod,DAAG-1,,In Progress
DAAG-4,daag,prod,DAAG-1,,Open
DAAG-5,BUG,prod,DAAG-1,,Open
DAAG-7,BUG,prod,DAAG-1,,Open
DAAG-8,daag,prod,DAAG-2,,Open

# [COLORS]: <color>,<color>,<color>,<color>,...
# Colors are applied to the alphabetized status list (e.g., [Closed, In Progress, Open])
# Default node color is lightgrey
# For a list of supported X11 colors see: https://graphviz.org/doc/info/colors.html#x11
[COLORS]: green,green:red,red
```
