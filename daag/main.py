from daag.misc import print_exception
from daag.parseargs import parse_args


def main() -> int:
    """Entry point for DAAG.

    Returns:
        0 on success, 1 on error/Exception.
    """
    # LOCAL VARIABLES
    retval = 0  # 0 for success, 1 on error
    db = None   # Path object for the input database

    try:
        db = parse_args()
    except Exception as err:
        print_exception(err)
        retval = 1

    # DONE
    return retval
