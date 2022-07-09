#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for i in my_list:
        average += (i[0] * i[1])
        size += (i[1])
    return (average / size)
