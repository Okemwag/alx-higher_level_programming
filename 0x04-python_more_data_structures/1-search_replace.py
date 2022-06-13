#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences of an element by another in a new list
    """
    new = my_list.copy()
    for run in range(len(new)):
        if new[run] == search:
            new[run] = replace
    return(new)
