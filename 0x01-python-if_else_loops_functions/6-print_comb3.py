#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit in range(digit1 + 1, 10):
        if digit1 == 8 and digit == 9:
            print("{}{}".format(digit1, digit))
        else:
            print("{}{},".format(digit1, digit), end=" ")
