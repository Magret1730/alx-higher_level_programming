#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if i < len(my_list):
            if idx < 0:
                return my_list
            elif i - 1 == idx:
                my_list[i - 1] = element  # insert element at i - 1
                return my_list
        else:
            return my_list
