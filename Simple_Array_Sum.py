# Given an array of integers, find the sum of its elements.

# For example, if the array , , so return .

class Solution:
    def simple_array_sum(self, n : list) -> int :
        a = n
        return sum(a)


if __name__ == '__main__':
    ob = Solution()
    val = ob.simple_array_sum([1,2,3])
    print(val)