#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_a = []
    for number in my_list:
        if number == search:
            number = replace
        list_a.append(number)
    return list_a
