#!/usr/bin/env python

fr = open('d:/AAAA.txt', 'r')
lineNum = 0
fileList = fr.readlines()
fr.close()
for item in fileList:
    if lineNum % 5 == 0:
        fileList.insert(lineNum, 'AAAAAAAAAAAA\n')
    lineNum += 1

fw = open('d:/AAAA.txt', 'w')
for item in fileList:
    fw.write(item)
    
fw.close()
            