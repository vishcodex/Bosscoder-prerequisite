from collections import defaultdict
import collections

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = collections.defaultdict(list)
        for num in nums:
            print("num is :", num)
            count[num] = count.get(num,0) + 1
            print("count is :", count)
        
        bucket = [[] for _ in range(len(nums) + 1)]
        print("bucket is :", bucket)
        for key in count:
            print("key is :", key)
            bucket[count[key]].append(key)
        res = []
        for freq in bucket:
            print("freq is :", freq)
            if freq:
                freq.sort(reverse = False) 
                print("freq after sort :", freq)
                for num in freq:
                    res += [num] * count[num]
        return res

#     def frequencySort(self, nums: list[int]) -> list[int]:
#         hashmap = defaultdict(int)
#         for i in nums:
#             hashmap[i]+=1 
#         return sorted(nums,key = lambda x: [hashmap[x], -x])



if __name__=='__main__':
    ob = Solution()
    val = ob.frequencySort([1,1,2,2,2,3])
    print(val)