#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for number in new_list:
        if (number == search):
            search_index = new_list.index(number)
            new_list[search_index] = replace
    return new_list
