"""Defines miscellaneous DAAG functionality."""
# Standard
import sys
# Third Party
# Local


def print_exception(error: Exception) -> str:
    """Standardizes exception messages and prints to stderr.

    Determines error exception type and formats the message with message_template.

    Args:
        error: Exception (or a class inherited from it) object.

    Returns:
        A string containing the formatted exception message.

    Raises:
        TypeError: error is not an Exception (or inherited from) type.
    """
    # LOCAL VARIABLES
    exception_type = ''                # Human-readable Exception type (e.g., Value)
    message_template = '{} ERROR: {}'  # Template message format
    exception_str = ''                 # Human-readable exception message
    formatted_msg = ''                 # End result message to return

    # INPUT VALIDATION
    if not isinstance(error, Exception):
        raise TypeError(f'The error argument must be of type Exception instead of {type(error)}')

    # FORMAT
    if isinstance(error, FileNotFoundError):
        exception_type = 'FILE'
    elif isinstance(error, OSError):
        exception_type = 'OS'
    elif isinstance(error, RuntimeError):
        exception_type = 'RUNTIME'
    elif isinstance(error, TypeError):
        exception_type = 'TYPE'
    elif isinstance(error, ValueError):
        exception_type = 'VALUE'
    else:
        exception_type = 'GENERAL'

    # PRINT
    # Str wrapper is important in case error.args[0] contains an errno value
    if isinstance(error, FileNotFoundError):
        exception_str = str(error)
    else:
        exception_str = str(error.args[0])
    formatted_msg = message_template.format(exception_type, exception_str)
    print(formatted_msg, file=sys.stderr)

    # DONE
    return formatted_msg
