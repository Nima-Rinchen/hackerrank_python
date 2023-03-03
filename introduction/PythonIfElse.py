"""
Input Format: A single line containing a positive integer, n
Output Format: Print Weird if the number is weird. Otherwise, print Not Weird.

"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print('Weird')
if n % 2 == 0:
    if n in range(2,6):
       print('Not Weird') 
    elif n in range(6,21):
       print('Weird')
    else:
       print('Not Weird')
