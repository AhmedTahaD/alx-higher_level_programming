#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    total_printed = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            total_printed += 1
        except IndexError:
            break
        print("")
        return (total_printed)
