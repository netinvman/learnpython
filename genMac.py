#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import random
macList = []
for i in range(1, 7):
    randStr = "".join(random.sample("0123456789abcdef", 2))
    macList.append(randStr)
    
randMac = ":".join(macList)
print randMac