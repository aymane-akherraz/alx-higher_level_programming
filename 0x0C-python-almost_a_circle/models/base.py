#!/usr/bin/python3
""" Define Base module """
import json
import os.path
import csv


class Base:
    """ Define a Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor.

        Args:
            id: An integer
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: a list of instances who inherits of Base
        """

        filename = "{}.json".format(cls.__name__)
        my_list = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                my_list.append(list_objs[i].to_dictionary())

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string

        Args:
            json_string: a string representing a list of dictionaries
        """

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set

        Args:
            dictionary: a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            new = cls(2, 3)
        else:
            new = cls(2)

        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """

        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', encoding="utf-8") as f:
            j_str = f.read()
        list_objs = cls.from_json_string(j_str)

        for i in range(len(list_objs)):
            list_objs[i] = cls.create(**list_objs[i])

        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in CSV

         Args:
            list_objs: a list of instances who inherits of Base
        """

        filename = "{}.csv".format(cls.__name__)
        if list_objs is not None:
            my_list = []
            for i in range(len(list_objs)):
                my_list.append(list_objs[i].to_dictionary())

        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']

        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            for obj in my_list:
                writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV """

        filename = "{}.csv".format(cls.__name__)
        list_objs = []
        with open(filename, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj_dict = {"id": int(row["id"]),
                                "width": int(row["width"]),
                                "height": int(row["height"]),
                                "x": int(row["x"]), "y": int(row["y"])}
                else:
                    obj_dict = {"id": int(row["id"]), "size": int(row["size"]),
                                "x": int(row["x"]), "y": int(row["y"])}
                list_objs.append(obj_dict)

            for i in range(len(list_objs)):
                list_objs[i] = cls.create(**list_objs[i])

        return list_objs
