#!/usr/bin/python3
""" Define a Student module """


class Student:
    """ Defines a student """
    def __init__(self, first_name, last_name, age):
        """
        Constructor

        Args:
            first_name: A string representing the first name of the student
            last_name: A string representing the last name of the student
            age: An integer representing the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """

        return self.__dict__
