# daunting-aggregate

Creates a directed graph based on an ingested database of backlog items.  Written in Python 3.10.

## Usage

`python -m daag -h`

## Database Example

```
# Title, Component, Type, Blocked By, Blocks, Status
DAAG-1,daag,prod,,,Closed
DAAG-2,wheel,devops,DAAG-1,,Open
DAAG-3,daag,prod,DAAG-1,,Open
DAAG-4,daag,prod,DAAG-1,,Open
DAAG-5,BUG,prod,DAAG-1,,Open
```
