#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):

    if not list_of_integers:
        return None
    
    middle = len(list_of_integers) // 2
    peak_candidate = list_of_integers[middle]

    if middle > 0:
        left_neighbor = list_of_integers[middle - 1]
    else:
        left_neighbor = float('-inf')

    if middle < len(list_of_integers) - 1:
        right_neighbor = list_of_integers[middle + 1]
    else:
        right_neighbor = float('-inf')

    if peak_candidate >= left_neighbor and peak_candidate >= right_neighbor:
        return peak_candidate
    elif peak_candidate < left_neighbor:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
