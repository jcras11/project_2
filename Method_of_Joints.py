#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:37:32 2021

@author: kendrick shepherd (and also Jacob Rasmussen woot woot, bust mostly Dr. Shepherd)
"""

import sys

import Geometry_Operations as geom

# Determine the unknown bars next to this node
def UnknownBars(node):
    list_of_unknown_bars = []
    for bar in node.bars:
        if bar.is_computed == False:
            list_of_unknown_bars.append(bar)
    return list_of_unknown_bars

# Determine if a node if "viable" or not
def NodeIsViable(node):
    return
    
# Compute unknown force in bar due to sum of the
# forces in the x direction
def SumOfForcesInLocalX(node, local_x_bar):
    return

# Compute unknown force in bar due to sum of the 
# forces in the y direction
def SumOfForcesInLocalY(node, unknown_bars):
    return
#Check for unknown forces
def UnknownMemberFinder(bars):
    for bar in bars:
        if bar.is_computed == False:
            return True
    return False
            
#def DoIHaveAnUnknownMember(nodes):
#    for node in nodes:
#        unknown_bars = UnknownBars(node)
#        if len(unknown_bars) >0:
#            return True
#    return False

# Perform the method of joints on the structure
def IterateUsingMethodOfJoints(nodes,bars):
    
    counter = 0
    
    while UnknownMemberFinder(bars) == True:
        
        
        BIGNUMBER = len(bars) +1
        counter += 1
        if counter > BIGNUMBER:
            sys.exit("Too many iterations")
    return bars