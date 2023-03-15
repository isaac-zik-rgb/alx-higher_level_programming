#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return(None)
    lagerst_num = my_list[0]
    for number in my_list:
        if number > lagerst_num:
            lagerst_num = number
    return(lagerst_num)
