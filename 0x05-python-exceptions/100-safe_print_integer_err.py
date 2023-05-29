#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return (True)
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
