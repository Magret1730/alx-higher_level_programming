#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if i < len(my_list):
            if idx < 0:
                return None
            elif idx == i - 1:
                return i
        else:
            return None
