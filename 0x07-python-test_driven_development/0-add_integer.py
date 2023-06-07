#!/usr/bin/python3
""" This module contains a function named add_integer"""

def add_integer(a, b):
    """
    Args:
        (a): The first parameter.
        (b): The second parameter.

    Returns:
        The return value of a + b. 
    
    Raises a type error if params is not float or int
    
    """
    
    if type(a) not in [int,float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int,float]:
        raise TypeError("b must be an integer")
     
    return int(a) + int(b)




