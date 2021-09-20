#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    target = s.split(":")
    if int(target[0]) < 12 and target[2][2:] == "PM":
        return str(int(target[0])+12)+":"+target[1]+":"+target[2][:2]
    if int(target[0]) >= 12 and target[2][2:] == "AM":
        if int(target[0])-12 == 0:
            return "0"+str(int(target[0])-12)+":"+target[1]+":"+target[2][:2]
        else:
            return str(int(target[0])-12)+":"+target[1]+":"+target[2][:2]
    return s[:len(s)-2]
