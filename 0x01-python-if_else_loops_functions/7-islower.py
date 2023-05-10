#!/usr/bin/python3
def isLower(c):
    if (ord(c) >= 97 and ord(c) <=  122):
        print("{:s} is lower".format(c))
        return True
    else:
        print("{:s} is upper".format(c))
        return False
