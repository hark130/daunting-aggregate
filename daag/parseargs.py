"""Defines DAAG's argument parser."""
# Standard Imports
from pathlib import Path
import argparse
# Third Party Imports
# Local Imports


def parse_args() -> Path:
    """Process the command line arguments.

    -h, --help                        show this help message and exit
    -d DATABASE, --database DATABASE  Filename of the input database

    Returns:
        Filename of the database file on success.

    Raises:
        FileNotFoundError: --database value not found
        OSError: --database value is not a file
        ValueError: Blank(?) --database value
    """
    # LOCAL VARIABLES
    parsed_args = None  # Parsed args as an argparse.Namespace object
    dbase = None        # Path object of the input database file
    # Object for parsing command line input into Python objects
    parser = argparse.ArgumentParser(prog='DAUNTING AGGREGATE (DAAG)')

    # ADD ARGUMENTS
    parser.add_argument('-d', '--database', action='store', required=True,
                        help='Filename of the input database')

    # PARSE ARGUMENTS
    parsed_args = parser.parse_args()

    # DB
    # Setup
    if not parsed_args.database:
        raise ValueError('--database entry may not be blank')
    dbase = Path(parsed_args.database)  # --database
    # Validate
    if not dbase.exists():
        raise FileNotFoundError(f'Unable to find {dbase.absolute()}')
    if not dbase.is_file():
        raise OSError(f'{dbase.absolute()} is not a file')

    # DONE
    return dbase
