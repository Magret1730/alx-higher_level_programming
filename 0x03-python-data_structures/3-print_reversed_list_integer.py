#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for element in my_list[::-1]:
        print("{}".format(element))
