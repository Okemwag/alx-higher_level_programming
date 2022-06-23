#!/usr/bin/python3


def list_division(my_list1, my_list2, list_length):
    temp_list = []
    for i in range(0, list_length):
        try:
            division = my_list[i] / my_list2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            temp_list.append(division)
    return temp_list
