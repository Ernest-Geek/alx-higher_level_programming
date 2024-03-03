#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        #indicating the followinf block may raise an exception
        try:
            print("{}".format(my_list[i]), end="")
        except:
            break
        else:
            count += 1
    print()
    return count
