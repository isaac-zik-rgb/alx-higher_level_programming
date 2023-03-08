#!/usr/bin/python3
for digit1 in range(1, 10):
    for digit in range(digit1 + 1, 9):
        if digit1 == 8 and digit == 9:
            print("{}{}".format(digit1, digit))
        elif digit1 != 7 or digit != 8:
            print("{}{},".format(digit1, digit), end=" ")
        else:
            print("{}{}".format(digit1, digit))
