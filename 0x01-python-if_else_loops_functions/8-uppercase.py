#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(str) >= 97 and ord(str) <= 122:
            ch = ord(str) - 32
            print("{}".format(ch), end="")
            print("")
