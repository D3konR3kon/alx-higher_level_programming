#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    c = 0
    d = 0

    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) < 2:
            if len(tuple_a) == 1:
                a = tuple_a[0]
        else:
            a = tuple_a[0]
            b = tuple_a[1]

        if len(tuple_b) < 2:
            if len(tuple_b) == 1:
                c = tuple_b[0]
        else:
            c = tuple_b[0]
            d = tuple_b[1]
    elif len(tuple_a) >= 2 or len(tuple_b) >= 2:
        a = tuple_a[0]
        b = tuple_a[1]
        c = tuple_b[0]
        d = tuple_b[1]

    total_1 = a + c
    total_2 = b + d
    t = total_1, total_2
    return t
