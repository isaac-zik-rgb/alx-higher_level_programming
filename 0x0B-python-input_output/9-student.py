#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """A class Student"""

    def __init__(self, first_name, last_name, age):
        """Args:
first_name (str) : the first name of the student
last_name (str): the last name of the student
age (int) : the age of the student
Returns:
the dictionary representation of the Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """that retruns the dictionary representation"""
        return self.__dict__
