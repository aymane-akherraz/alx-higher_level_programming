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

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """

        if type(attrs) == list and all(isinstance(e, str) for e in attrs):
            filted_dict = {}
            for el in attrs:
                if el in self.__dict__:
                    filted_dict[el] = self.__dict__[el]

            return filted_dict

        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance

        Args:
            json: A dictionary
        """

        for k, v in json.items():
            setattr(self, k, v)
