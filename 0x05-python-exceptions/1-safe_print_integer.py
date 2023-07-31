#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is int:
            print("{}".format(value), end="")
            return True
    except ValueError:
        return False
