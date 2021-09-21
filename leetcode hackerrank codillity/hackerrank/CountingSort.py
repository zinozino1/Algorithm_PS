#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    n = len(arr)
    tmp = [0]*(100)
    for i in range(n):
        tmp[arr[i]] += 1

    return tmp
