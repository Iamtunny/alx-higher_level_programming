#!/usr/bin/python3
for j in range(0, 10):
    for i in range(j+1, 10):
        if j == 8 and i == 9:
            print(f"{j}{i}".format(j, i))
        else:
            print(f"{j}{i},".format(u, d), end=" ")
