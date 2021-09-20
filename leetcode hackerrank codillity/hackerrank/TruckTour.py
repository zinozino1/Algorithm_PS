#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)
    cost = []
    for petro in petrolpumps:
        cost.append(petro[0] - petro[1])

    for i, petro in enumerate(petrolpumps):
        if cost[i] < 0:
            continue

        sum = cost[i]
        idx = (i+1) % n
        while i != idx:
            sum += cost[idx]
            if sum < 0:
                break
            idx = (idx+1) % n
        else:
            return i
