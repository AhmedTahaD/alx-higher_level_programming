#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 == 0:
        minus = 0
    else:
        minus = 32
    print('{}'.format(chr(letter - minus)), end='')
