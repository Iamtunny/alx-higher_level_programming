if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    if number == 1:
        print("0 arguments.")
    elif number == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(number - 1))
        for j in range(number - 1):
            print("{}: {}".format(j + 1, sys.argv[j + 1]))
