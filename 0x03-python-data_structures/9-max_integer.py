#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        maximum = my_list[0]
        for x in my_list:
            if x > maximum:
                max = x
        return max
    else:
        return None

