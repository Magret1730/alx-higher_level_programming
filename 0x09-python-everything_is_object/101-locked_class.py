#!/usr/bin/python3
"""A class LockedClass

a class LockedClass with no class or object attribute, that prevents the
user from dynamically creating new instance attributes, except if the new
instance attribute is called first_name.
"""


class LockedClass:
    """a class LockedClass with no class or object attribute"""

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """prevents the user from dynamically creating new instance attributes

        except if the new instance attribute is called first_name.
        """

        if name != 'first_name':
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
