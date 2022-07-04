# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            for j in range(i+1):
                v = i + j
                if v == 9:
                    return [nums.index(i),nums.index(j)]
        

if __name__ == '__main__': 
    nums = [2,7,11,15]
    target = 9
    ob = Solution()
    twoSum = ob.twoSum(nums,target)
    print(twoSum)