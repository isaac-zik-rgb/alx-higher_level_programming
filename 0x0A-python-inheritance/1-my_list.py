#!/usr/bin/python3

"""Define a class Mylist"""


class MyList(list):
    """A subclass to list"""

    def __init__(self):
        """initializing the object"""
        super().__init__()


    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
