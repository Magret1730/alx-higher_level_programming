#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""


class Node:
    """A private instance attribute data and next_node created"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """A private instance attribute data whose value must be an integer"""

        self.head = None

    def __str__(self):
        """Converting to string"""

        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()

    def sorted_insert(self, value):
        """A public instance method

        that inserts a new Node into the correct sorted position in
        the list (increasing order)
        """

        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and\
                    value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
