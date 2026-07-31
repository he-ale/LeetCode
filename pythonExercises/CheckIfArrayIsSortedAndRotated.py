from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        last= nums[-1]
        i= len(nums)-2
        while (i >= 0):
            if (last < nums[i]):
                break
            last= nums[i]
            i-=1

        if (i==-1):
            return True

        return self.__check__(nums[i+1:]+nums[:i+1])

    def __check__(self, nums: List[int]) -> bool:
        last= nums[-1]
        i= len(nums)-2
        while (i >= 0):
            if (last < nums[i]):
                break
            last= nums[i]
            i-=1

        return i==-1

s= Solution()

s.check([2,1,3,4])


