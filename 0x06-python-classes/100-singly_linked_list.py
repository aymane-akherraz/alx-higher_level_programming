#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """Define a node"""
    def __init__(self, data, next_node=None):
        """
        Constructor.

        Args:
            data: an integer representing the data to be
            inserted to the new Node
            next_node: the next node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node to the given value

        Raises:
            TypeError: if value is not an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node data to the given value

        Raises:
            TypeError: if value is not an integer
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a SinglyLinkedList"""

    def __init__(self):
        """
        Constructor.

        Attributes:
        head: head of the SinglyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value: the value to insert to the new node data
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif value <= self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            ptr = self.__head
            while (ptr.next_node is not None and
                    value > ptr.next_node.data):
                ptr = ptr.next_node
            new.next_node = ptr.next_node
            ptr.next_node = new

    def __str__(self):
        """Print the entire list in stdout one node number by line"""
        node_list = []
        ptr = self.__head
        while ptr:
            node_list.append(str(ptr.data))
            ptr = ptr.next_node
        return "\n".join(node_list)
