# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:22:09 2016

@author: Shaun
"""

import numpy as np
import random

def minbar(target, racklist):
    barlist = []
    remainder = target
    while remainder <> 0:
        maxweight = max(racklist)
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

def randomchoose(target, barlist, racklist):
    """
    Randomly start loading the bar until the target weight is met
    """

    remaining = target - sum(barlist)
    counter = 0
    while remaining >= 0:
        plate = random.choice(racklist)
        print "Choosing plate ", plate, " remaining ", remaining
        if plate <= remaining:
            barlist.append(plate)
            racklist.remove(plate)
            remaining = remaining - plate
            print "Added ", plate
            print "remaining ", remaining
            print "racklist", racklist
            if remaining//min(racklist)*min(racklist) != remaining:
                # there isn't going to be a way of completing this,
                # so remove last plate
                barlist.remove(plate)
                racklist.add(plate)
                remaining = remaining + plate
            #print "HERE"
        remaining = target - sum(barlist)
        counter += 1
        if counter > 1000:
            print "spun out"
            break

def emptybar(barlist,racklist):
    for plate in barlist:
        barlist.remove(plate)
        racklist.append(plate)
    #racklist.sort(reverse=True)

racklist = [20,20,10,5,5,2.5,2.5,1.25,1.25]
barlist = []

#randomload(41.25,barlist,racklist)
#print sorted(racklist)
#print sorted(barlist), sum(barlist)
