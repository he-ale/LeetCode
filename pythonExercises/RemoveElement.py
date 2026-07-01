from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i= 0
        j= 0
        for num in nums:
            if (num!=val):
                nums[i]= nums[j]
                i+=1
            j+=1
        return i


