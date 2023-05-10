#!/usr/bin/python3
for x in range(9):
    for y in range(10):
        if x < y:
            print("{:d}{:d}".format(x % 10, y % 10), end="")
            if x == 8 and y == 9:
                print()
                break
            print(", ", end="")
