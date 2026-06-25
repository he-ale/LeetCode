from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        aux= set(nums)
        return len(nums)>len(aux)
