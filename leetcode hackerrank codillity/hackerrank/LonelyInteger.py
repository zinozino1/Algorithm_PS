#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    dic = dict()

    for i in a:
        if not dic.get(i):
            dic[i] = 1
        else:
            dic[i] += 1
    for key in dic.keys():
        if dic[key] == 1:
            return key
