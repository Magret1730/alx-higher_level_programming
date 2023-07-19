#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        # for values in range(len(my_list)):
#            if my_list[values] == search:
#                my_list[values] = replace
        my_list = [replace if element == search else element for element in my_list]
    return my_list
