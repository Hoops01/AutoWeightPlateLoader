# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:22:09 2016

@author: Shaun
"""

import numpy as np

def minbar(target, racklist):
    barlist = []
    remainder = target
    while remainder <> 0:
        print racklist
        maxweight = max(racklist)
        print maxweight
        if maxweight <= remainder:
            # Yes, then add maxweight to bar and remove from rack
            remainder = remainder - maxweight
            barlist.append(maxweight)
            print "Added ", maxweight, "to bar, ", remainder, "to go"
        racklist.remove(maxweight)
        
    return barlist
    
def addbar(target, barlist, racklist):
    discardlist = []
    onbar = sum(barlist)
    remainder = target - onbar
    while remainder <> 0:
        maxplate = max(racklist)
        if maxplate <= remainder:
            # Add max plate to bar and remover from rack
            barlist.append(maxplate)
            remainder = remainder - maxplate
            print "Added ", maxplate, "to bar, ", remainder, "to go"
        racklist.remove(maxplate)
        discardlist.append(maxplate)
    
    print barlist
    print racklist
    print discardlist
    racklist = racklist + discardlist
    print racklist
    return

def randomload(target, barlist, racklist):
    import random
    onbar = sum(barlist)
    counter = 0
    while onbar != target:
        onbar = sum(barlist)
        remaining = target - onbar
        r = random.choice(racklist)
        if r <= remaining:
            barlist.append(r)
            racklist.remove(r)
        counter += 1
        if counter > 1000:
            break

racklist = [20,20,10,5,5,2.5,2.5,1.25,1.25]
barlist = []

randomload(41.25,barlist,racklist)
print sorted(racklist)
print sorted(barlist), sum(barlist)
