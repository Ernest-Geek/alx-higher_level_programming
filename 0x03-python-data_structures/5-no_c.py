#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    #Keep track of the number of characters been removed
    i = 0

    #create a shallow copy of the original string
    new_string = my_string[:]

    for j in range(length):
        if(my_string[j] == 'c' or my_string[j] == 'C'):
            new_string = new_string[:(j-i)] + my_string[(j+1):]
            i += 1
    return new_string

