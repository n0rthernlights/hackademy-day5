# Write a function `remove_duplicates` that takes
# in a list and returns a list without duplicates.
# For example:
# `remove_duplicates([1,1,2,2])` should return `[1,2]`.

def remove_duplicates(a_list):
    b_list = [a_list[0]]
    for i in a_list:
        if i in b_list:
            continue
        else:
            b_list.append(i)
    return b_list

def square_numbers(a_list):
    b_list = []
    for i in a_list: 
        a = i * i
        b_list.append(a)
    return b_list
