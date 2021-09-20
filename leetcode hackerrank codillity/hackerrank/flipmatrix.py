#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    res = 0
    n = len(matrix)
    for i in range(n//2):
        for j in range(n//2):
            res += max(matrix[i][j], matrix[n-i-1][j],
                       matrix[i][n-j-1], matrix[n-i-1][n-j-1])
    return res

