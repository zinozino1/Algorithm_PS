#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    grid = [list(g) for g in grid]

    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(grid[i][j])
        tmp.sort()
        for j in range(m):
            grid[i][j] = tmp.pop(0)

    for i in range(m):
        for j in range(n-1):
            if grid[j+1][i] < grid[j][i]:
                return "NO"
    return "YES"
