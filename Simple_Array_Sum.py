# Given an array of integers, find the sum of its elements.

# For example, if the array , , so return .
import math
import os
import random
import re
import sys

class Solution:
    def simpleArraySum(self, n : list) -> int :
        a = n
        return sum(a)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = map(int, input().rstrip().split())
    ob = Solution()
    val = ob.simpleArraySum(ar)
    print(val)