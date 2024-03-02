#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #create a shallow copy of the initial list
    new_list = []

    #Iterate over each item in the list
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list
