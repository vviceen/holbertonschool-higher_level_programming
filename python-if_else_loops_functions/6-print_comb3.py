#!/usr/bin/python3
for iterator in range(10):
    for scnd_itr in range(0, 10):
        if iterator < scnd_itr:
            print(str(iterator) + str(scnd_itr), end=", ")
