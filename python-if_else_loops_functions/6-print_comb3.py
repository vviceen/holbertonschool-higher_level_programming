#!/usr/bin/python3
for iterator in range(10):
    for scnd_itr in range(0, 10):
        if iterator < scnd_itr:
            if iterator == 8 and scnd_itr == 9:
                continue
            print("{}{}".format(iterator, scnd_itr), end=", ")
print("89")