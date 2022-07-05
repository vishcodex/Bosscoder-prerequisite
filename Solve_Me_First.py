# Complete the function solveMeFirst to compute the sum of two integers.
# Example
# Return 10

class Solution:
    def solveMeFirst(self, a, b):
	# Hint: Type return a+b below
        return a + b


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    ob = Solution()
    res = ob.solveMeFirst(num1,num2)
    print(res)