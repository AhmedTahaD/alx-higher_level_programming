#!/usr/bin/python3
def complex_delete(my_dict, value):
    temp = my_dict.copy()
    for i, j in temp.items():
        if value == j:
            my_dict.pop(i)
    return my_dict
