#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        for values in range(len(my_list)):
            if my_list[values] == search:
                if search is None:
                    return my_list
                if replace is None:
                    return my_list
                my_list[values] = replace
        return my_list
    else:
        return my_list
