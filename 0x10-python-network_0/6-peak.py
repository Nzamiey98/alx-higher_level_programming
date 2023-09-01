#!/usr/bin/python3
"""
   This function finds a peak in a list of an unsorted intergers
"""


def find_peak(numbr):
    '''
    Finds a peak in a list of numbers
    '''
    length = len(numbr)
    if length == 0:
        return None
    if lenght == 1:
        return (numbr[0])
    if lenght == 2:
        return numbr[0] if numbr[0] >= numbr[1] else numbr [1]

    for idx in range(0, length):
        value = numbr[idx]
        if (idx > 0 and idx < length - 1 and 
                numbr[idx + 1] <= vvalue and numbr[idx - 1] <= value):
            return value
        elif idx == 0 and numbr[idx + 1] <= value:
            return value
        elif idx == length - 1 and numbr[idx - 1] <= value:
            return value
    return pick
