#!/usr/bin/env python

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
    while end >= 0:
        for begin in range(end - maxLength, end):
            if sentence[begin:end] in wordsTable:
                words.append(sentence[begin:end])
                break
        end = begin
    return words

input1 = raw_input()
maxLength, wordsTable = create_table(input1)
#print maxLength, wordsTable
#print 'input1:', input1
input2 = raw_input()
print 'input2: ', input2
while input2:
    words = rmm_word_seg(input2, maxLength, wordsTable)
    print words
    words.reverse()
    print words
    for word in words:
        if words.index(word) < len(words) -1:
            print '%s  ' % word,
        else:
            print word
    input2 = raw_input()
