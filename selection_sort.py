#!/usr/bin/env python

def swap(lst, i , j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def selection_sort_v1(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst.insert(i, lst.pop(min_index))
    return lst

def selection_sort_v2(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        swap(lst, i, min_index)
    return lst
                

lst = [12, 10, 5, 8, 9, 1]
print selection_sort_v2(lst)