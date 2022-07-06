# Given N,  reverse the digits of N.

#User function Template for python3

from math import remainder


class Solution:
    def reverse_digit(self, n):
        # Code here
        rev = 0
        while n != 0:
            remainder = n % 10
            rev = rev * 10 + remainder
            n = n // 10
        return rev

if __name__ == '__main__':
    # T=int(input())
    # for i in range(T):
    n = int(input())
    ob = Solution()
    ans = ob.reverse_digit(n)
    print(ans)