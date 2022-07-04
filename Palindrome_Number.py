# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        orignal_val = x
        rev_val=0
        while(x>0):
            last_val=x%10
            rev_val = rev_val*10+last_val
            x = x // 10
        if(orignal_val==rev_val):
            return True
        else:
            return False

if __name__ == '__main__':
    ob = Solution()
    val = ob.isPalindrome(x = 10)
    print(val)
