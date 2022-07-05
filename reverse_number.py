

class Solution:
    def reverse_number(self, num: int) -> int :
        print("Need to print the number in reverse!")
        n = 0
        last_val = 0
        rev_num = 0
        while num != 0:
            last_val = num%10
            rev_num = rev_num * 10 + last_val
            num = num // 10
        return rev_num

if __name__ == '__main__':
    ob = Solution()
    val = ob.reverse_number(2345)
    print(val)
