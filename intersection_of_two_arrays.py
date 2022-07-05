# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        print("sol")
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
        return list(set(res))


if __name__ == '__main__':
    ob = Solution()
    val = ob.intersection([1,2,2,1],[2,2])
    print(val)