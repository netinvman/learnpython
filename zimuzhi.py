#!/usr/bin/env python

chars = 'abcdefghijklmnopqrstuvwxyz'

while True:
    sum = 0
    inputStr = raw_input()
    if inputStr:
        for char in inputStr:
            if char.lower() in chars:
                sum += chars.index(char.lower()) + 1
        
        print sum
    else:
        break
