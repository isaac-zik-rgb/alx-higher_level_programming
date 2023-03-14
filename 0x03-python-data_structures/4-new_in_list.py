#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return(my_list)
    for i in list(my_list):
        if i == idx:
            my_list[indx] = element
            return(my_list)
