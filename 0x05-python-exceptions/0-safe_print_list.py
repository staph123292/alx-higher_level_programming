#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tracker = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            tracker = tracker + 1
        except IndexError:
            break
    print("")
    return tracker
