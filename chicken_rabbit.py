#!/usr/bin/env python

for chicken in range(36):
    for rabbit in range(36):
        if chicken + rabbit == 35 and 2 * chicken + 4 * rabbit == 94:
            print 'chicken:', chicken
            print 'rabbit:', rabbit
