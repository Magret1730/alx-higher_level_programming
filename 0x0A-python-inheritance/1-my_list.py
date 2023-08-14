#!/usr/bin/python3
"""A module"""


class MyList(list):
    """child class that inherits from class list"""

    def print_sorted(self):
        """
        public instance method that prints the list,
        but sorted (ascending sort)
        """

        # MyList inherited list built-in class
        print(sorted(self))
