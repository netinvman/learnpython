#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# Author: Yellow
# Date: 2015/02/28
# File: genMac.py

import random
macList = []
for i in range(1, 7):
    randStr = "".join(random.sample("0123456789abcdef", 2))
    macList.append(randStr)
    
randMac = ":".join(macList)
print randMac
