#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return (True)
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
