#!/usr/bin/python3
"""A module"""


class MyInt(int):
    """inherits from module int with inverted equality operators"""

    def __eq__(self, other):
        """changes == to !="""

        return super().__ne__(other)

    def __ne__(self, other):
        """changes != to =="""

        return super().__eq__(other)
