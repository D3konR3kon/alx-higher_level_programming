#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        int(value)
    except:
        Exception
