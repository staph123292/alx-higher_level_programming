#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Find  finds all multiples of 2 in a list
    return list(map(lambda x: True if x % 2 == 0 else False, my_list))
