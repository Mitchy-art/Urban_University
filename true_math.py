import math


def divide(first, second):
    if second != 0:
        result = first/second
        return result
    if second == 0:
        from math import inf
        return inf
