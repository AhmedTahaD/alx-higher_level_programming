#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list) - 1
    if idx < 0 or idx > list_len:
        return(my_list)
    else:
        del my_list[idx]
        return (my_list)
