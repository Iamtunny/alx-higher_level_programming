#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if 97 <= ord(a) <= 122:
            a = chr(ord(a) - 32)
            print("{}".format(a), end="")
            print("")
