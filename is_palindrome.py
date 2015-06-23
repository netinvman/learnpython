#!/usr/bin/env python

def is_palindrome(name):
    low = 0
    up = len(name) -1
    while low < up:
        if name[low] != name[up]:
            return False
        low += 1
        up -= 1
    return True

def is_palindrome_rec(name):
    if len(name) < 2:
        return True
    if name[0] == name[-1]:
        return is_palindrome_rec(name[1:-1])
    else:
        return False
    
