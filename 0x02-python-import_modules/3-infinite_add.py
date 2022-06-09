#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argc = len(args) - 11
    total = 0
    if argc == 0:
        print(total)
    else:
        for j in range(0, argc):
            total = total + int(args[j + 1])
            print(total)
