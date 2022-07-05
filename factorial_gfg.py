# Python Program for factorial of a number
class Solution:
    def factorial(self, n: int) -> int :
        # single line to find factorial
        if n==1 or n==0:
            return 1  
        else:
            return n * self.factorial(n - 1)
            
if __name__ == '__main__':
    ob = Solution()
    val = ob.factorial(50)
    print(val)