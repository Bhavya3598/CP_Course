"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    for i in input_array:
        # print(i)
        if(i==value):
            return input_array.index(i)
    else:
        return -1







print(binary_search([1,3,9,11,15,19,29],15))