#!/usr/bin/env python

def load_dict(filename):
    word_dict = set()
    f = open(filename)
    max_len = 1
    for line in f:
        word = unicode(line, 'utf-8')
        word_dict.add(word)
        if len(word) > max_len:
            max_len = len(word)
    f.close()
    return max_len, word_dict

def fmm_word_seg(sentence, max_len, word_dict):
    begin = 0
    words = []
    while begin < len(sentence):
        for end in range(begin + max_len, begin, -1):
            if sentence[begin:end] in word_dict:
                words.append(sentence[begin:end])
                break
        begin = end
    return words
sentence = raw_input('inut a sentence: ')
sentence = unicode(sentence, 'utf-8')
max_len, word_dict = load_dict('lexicon.dic')
words = fmm_word_seg(sentence, max_len, word_dict)
for word in words:
    print word