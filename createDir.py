# _*_ coding: utf-8 _*_
#!/usr/bin/env python

import os
sourceDir = 'd:/test'
destDir = 'd:/newdir'
fileList = []
for root, dirs, files in os.walk(sourceDir):
    for file in files:
        fileList.append(file.split('_')[1].split('.')[0])

for fileName in fileList:
    filePath = destDir + os.sep + fileName
    if not os.path.exists(filePath):
        os.mkdir(filePath)
        print 'successfully created directory: ', filePath
        
