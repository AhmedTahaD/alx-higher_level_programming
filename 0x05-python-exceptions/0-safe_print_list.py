#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total_printed = 0

    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            total_printed += 1
        except:
            continue
        print("")
        return (total_printed)
