#!/usr/bin/python3
# def divisible_by_2(my_list=[]):
#    if my_list is not None:
#        new_list = []
#        for element in my_list:
#            if element % 2 == 0:
#                new_list = new_list + [True]
#            else:
#                new_list = new_list + [False]
#            return new_list

def divisible_by_2(my_list=[]):
    if my_list is not None:
        result_list = []
        for element in my_list:
            result_list.append(element % 2 == 0)
        return result_list
