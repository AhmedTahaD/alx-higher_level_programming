#!/usr/bin/python3
def no_c(my_string):
    letters = list(my_string)
    for letter in letters:
        if letter == 'c' or letter == 'C':
            letters.remove(letter)
    return("".join(letters))
