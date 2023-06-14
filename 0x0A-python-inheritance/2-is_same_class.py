#!/usr/bin/python3
"""Defines a class-checking function."""
def is_same_class(obj, a_class):
    """
    ARGS:
        * obj: object to verify
        * a_class: verify if this class is the class of obj
    """
    if type(obj) is a_class:
        return (True)
    return (False)
