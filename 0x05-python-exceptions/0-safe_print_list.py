#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for j in range(x):
        try:
            print(my_lisst[j], end="")
            n += 1
        except IndexError:
            print("", end="")
    print()
    return n
