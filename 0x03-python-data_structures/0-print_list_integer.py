#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # Define a function that prints all int
    for n in range(len(my_list)):
        print('{:d}'.format(my_list[n]))
