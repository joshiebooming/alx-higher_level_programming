#!/usr/bin/python3
def safe_print_integer(value):
    """code that prints an integer with "{:d}".format()
    Args:
      value(int)
    Return:
        True -if value is an int
	else False"""
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
