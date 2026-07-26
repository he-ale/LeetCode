from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i= 0
        j= len(nums)-1
        k= 0
        while (i <= j):
            k= (j + i)//2
            if (nums[k] == target):
                return k
            elif (nums[k] > target):
                j= k-1
            else:
                i= k+1
        if nums[k]>target:
            return k
        return k+1