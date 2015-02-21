# author: Yellow
# date: 2015/2/21
#!/usr/bin/env python

for i in range(1, 10):
    for j in range(1, i + 1):
        if j == i:
            print '%dx%d=%d' % (j, i, j * i)
        else:
            print '%dx%d=%d\t' % (j, i, j * i),
    print
    
