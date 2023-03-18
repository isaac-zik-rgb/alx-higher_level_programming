#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictiomary.keys())
    for valu_key in list_keys:
        if value == a_dictionary.get(valu_key):
            del a_dictionary[valu_key]
    return(a_dictionary)
