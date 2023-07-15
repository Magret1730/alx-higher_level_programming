#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in my_list:
        # this_list = my_list.copy()
        this_list = my_list[:]
        if i < len(my_list):
            if idx < 0:
                return this_list
            if idx == i - 1:
                this_list[i - 1] = element
                return this_list
        else:
            return this_list  # copy of original list
