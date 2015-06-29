#!/usr/bin/env python

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def bubble_sort(lst):
    top = len(lst) - 1
    is_exchange = True
    while is_exchange:
        is_exchange = False
        for i in range(top):
            if lst[i] > lst[i + 1]:
                swap(lst, i, i + 1)
                is_exchange = True
        top -= 1
    return lst
            
lst = [12, 10, 1, 5, 9, 8, 6]
print bubble_sort(lst)