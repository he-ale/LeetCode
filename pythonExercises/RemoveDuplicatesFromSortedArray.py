from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j= 1
        counter=1
        current= nums[0]
        for i in range(1, len(nums)):
            if (nums[i]!=current):
                nums[j]=nums[i]
                current= nums[i]
                counter+=1
                j+=1
        print(nums)
        return counter
    
s= Solution()

print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        