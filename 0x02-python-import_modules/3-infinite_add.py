#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    number = len(sys.argv)
    if number == 1:
        print("0")
    else:
        for j in range(1, number):
            sum += int(sys.argv[j])
            print("{}".format(sum))
