#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for values in range(len(my_list)):
        if my_list[values] == search:
            my_list[values] = replace
    return my_list
