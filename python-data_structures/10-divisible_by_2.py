#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    other_list = []
    for number in my_list:
        if number % 2 == 0:
            other_list += [True]
        else:
            other_list += [False]
    return other_list
