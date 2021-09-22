#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    res = ''
    a, A = [], []
    for i in range(26):
        A.append(chr(i+65))
        a.append(chr(i+97))
    for _ in range(k):
        A.append(A.pop(0))
        a.append(a.pop(0))

    for c in s:
        if c.isalpha():
            if c.isupper():
                res += A[ord(c)-65]
            else:
                res += a[ord(c)-97]
        else:
            res += c
    return res
