#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.
    Args:
        my_list (list): this the list  print elements from
        x (int):number of elements of my list to print
    Returns:
        The number of elemets printted"""
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return(ret)
