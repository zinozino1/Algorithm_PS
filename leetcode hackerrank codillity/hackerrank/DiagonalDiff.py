#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    left = 0
    right = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                left += arr[i][j]
            if n-j-1 == i:
                right += arr[i][j]
    return abs(left-right)

