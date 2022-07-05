# Alice and Bob each created one problem for HackerRank. 
# A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    result = []
    alice_counter = 0
    bob_counter = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_counter += 1
        elif a[i] < b[i]:
            bob_counter += 1
        else:
            continue
    return [alice_counter,bob_counter]


if __name__ == '__main__':

    # fptr = open('/home/user/', 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    print("a is :", a, type(a))
    print("b is :", b, type(b))

    result = compareTriplets(a, b)

    print(result)


    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()