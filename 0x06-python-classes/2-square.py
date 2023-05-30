#!/usr/bin/python3

"""
Creating Square class 
"""

class Square:
    """
    class Square consructor
    """

    def __init__(self, size = 0):

        """ __size is private """

        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
