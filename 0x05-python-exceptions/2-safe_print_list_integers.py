#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            Pass
       #except IndexError:
           #print("Wrong indexing. Please try again")
    return count
