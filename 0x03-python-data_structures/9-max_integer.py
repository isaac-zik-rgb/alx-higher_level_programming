#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    lagerst_num = my_list[0]
    for number in range(len(my_list)):
        if my_list[number] > lagerst_num:
            lagerst_nun = my_list[number]
    return(lagerst_num)
