#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    pos, neg, zero = 0, 0, 0
    for a in arr:
        if a > 0:
            pos += 1
        elif a == 0:
            zero += 1
        else:
            neg += 1

    res = []
    for nxt in [pos, neg, zero]:
        if nxt == 0:
            res.append(0)
        else:
            res.append(round(nxt/len(arr), 6))
    for r in res:
        print(r)
