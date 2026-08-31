from typing import List, Callable

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if(len(nums) == 1):
            return True

        if(nums[0]<nums[len(nums)-1]):
            return self.__isMonotonic__(nums, lambda a, b: a <= b)
        else:
            return self.__isMonotonic__(nums, lambda a, b: a >= b)

    def __isMonotonic__(self, nums: List[int], function: Callable[[int, int], bool]):
        for i in range(1, len(nums)):
            if (not function(nums[i-1], nums[i])):
                return False
        return True