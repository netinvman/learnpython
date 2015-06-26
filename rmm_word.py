#!/usr/bin/env python
#coding: utf-8

def create_table(inputStr):
    wordsTable = set()
    maxLength = 1
    for word in inputStr.split():
        word = unicode(word, 'utf-8')
        wordsTable.add(word)
        if maxLength < len(word):
            maxLength = len(word)
    return maxLength, wordsTable

def rmm_word_seg(sentence, maxLength, wordsTable):
    end = len(sentence)
    words = []
    sentence = unicode(sentence, 'utf-8')
    while end >= 0:
        for begin in range(end - maxLength, end):
            if sentence[begin:end] in wordsTable:
                words.append(sentence[begin:end])
                break
        end = begin
    return words

input1 = raw_input()
maxLength, wordsTable = create_table(input1)
input2 = raw_input()
input2 = unicode(input2)
while input2:
    words = rmm_word_seg(input2, maxLength, wordsTable)
    words.reverse()
    for word in words:
        if words.index(word) < len(words) -1:
            print '%s  ' % word,
        else:
            print word
    input2 = raw_input()
