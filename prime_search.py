#!/usr/bin/env python

def prime(n):
    primeList = []
    if n < 2:
        return []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primeList.append(i)
    return primeList

def bi_search(num):
    pass

print prime(20)
