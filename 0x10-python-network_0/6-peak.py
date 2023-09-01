#!/usr/bin/python3

def find_peak(list_of_integers):
    """
find_peak - A function that find the peak of list of numbers passed to it
Args:
@list_of_intergers: the list of numbers passed to it
"""
    if list_of_integers is None or list_of_integers == []:
        return None
    first = 0
    last = len(list_of_integers)
    mid = ((last + first) // 2) + first
    mid = int(mid)
    if last == 1:
        return list_of_integers[0]
    if last == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
       list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
