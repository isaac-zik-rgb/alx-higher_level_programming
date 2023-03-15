#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """find all multiply of 2 in the list"""
    multiply = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiply.append(True)
        else:
            multiply.append(False)
    return(multiply)
