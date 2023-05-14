#!/usr/bin/python3

def element_at(myList, i):
    
    if i < 0:
        return None
    
    if i > len(myList):
        return None
    
    return myList[i]
