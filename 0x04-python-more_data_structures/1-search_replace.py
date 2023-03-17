#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        new_list = my_list.replace(search, replace)
    return(new_list)
