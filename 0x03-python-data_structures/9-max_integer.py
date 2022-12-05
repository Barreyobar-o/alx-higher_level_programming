#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        num = min(my_list)
        for i in my_list:
            if i > num:
                num = i
        return num
