#!/usr/bin/python3

"""Function that finds a peak element in a list"""


def find_peak(list_of_integers):

    """Finds a peak element in the list,
    which is greater than its neighbors."""

    if not list_of_integers:  # Handle empty list
        return None

    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers) - 1):
        # Iterate up to second-to-last element
        if list_of_integers[i] > list_of_integers[i - 1] and \
                list_of_integers[i] > list_of_integers[i + 1]:
            peak = list_of_integers[i]
            break  # Found a peak, no need to continue

    return peak
