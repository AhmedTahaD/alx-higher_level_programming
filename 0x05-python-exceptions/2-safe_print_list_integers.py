#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    total_printed = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            total_printed += 1
        except (ValueError, TypeError):
            pass
        index += 1
    print()
    return total_printed
