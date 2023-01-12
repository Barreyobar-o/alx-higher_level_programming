#!/usr/bin/python3
""" Pascalm triangle function """


def pascal_triangle(n):
    """ return the pascal triangle in lists """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_list = pascal_triangle(n - 1)
        cur_row = [1]
        prev_row = new_list[-1]
        for i in range(len(prev_row)-1):
            cur_row.append(prev_row[i] + prev_row[i + 1])
        cur_row += [1]
        new_list.append(cur_row)
        return new_list
