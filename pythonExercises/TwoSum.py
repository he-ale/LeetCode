from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values= {}
        rs=[]
        for i in range(len(nums)):
            aux= target-nums[i]
            if aux in values:
                rs= [values[aux], i]
                break
            values[nums[i]]=i          
        return rs
    
solution= Solution()

print(solution.twoSum([2,7,11,15], 9))
