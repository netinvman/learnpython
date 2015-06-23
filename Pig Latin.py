#!/usr/bin/env python

input_str = raw_input()
input_str = input_str.lower()


for word in input_str.split():
    if word.startswith(('a', 'e', 'i', 'o', 'u')):
        print word + 'hay',
    elif word.startswith('qu'):
        print word[2:] + 'quay',
    else:
        for w in word:
            if w in 'aeiou' or (w == 'y' and word.index(w) != 0):
                print word[word.index(w):] + word[:word.index(w)] + 'ay',
                break
        else:
            print word + 'ay',

