#!/usr/bin/python3

def find_peak(list_of_integers):
    """
find_peak - A function that find the peak of list of numbers passed to it
Args:
@list_of_intergers: the list of numbers passed to it
"""
    list_of_integers.sort(reverse=True)
    firstNum = list_of_integers[1]
    for i in list_of_integers:
        if i == firstNum:
            return i, firstNum
        else:
            return list_of_integers[0]
