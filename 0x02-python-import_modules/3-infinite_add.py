#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    length = len(sys.argv) - 1
    for i in range(length):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
