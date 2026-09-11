from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary= dict()
        for i in range(k+1):
            if (i == len(nums)):
                break
            elif (nums[i] in dictionary):
                return True
            else:
                dictionary[nums[i]]= i

        m= 0
        for j in range(k+1, len(nums)):
            if (j >= len(nums)):
                break
            del dictionary[nums[m]]
            if (nums[j] in dictionary):
                return True
            else:
                dictionary[nums[j]]= j
            m+= 1
        return False  