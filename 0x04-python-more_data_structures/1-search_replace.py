#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        return [replace if element == search else element
                for element in my_list]
