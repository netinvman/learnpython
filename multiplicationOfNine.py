#!/usr/bin/env python

for i in range(1, 10):
    for j in range(1, i + 1):
        print '%d x %d = %d' % (j, i, j * i)
    print
    
