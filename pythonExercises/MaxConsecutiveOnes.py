from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes= 0
        aux= 0
        for num in nums:
            if (num == 1):
                aux+= 1
            else:
                maxOnes= max(maxOnes, aux)
                aux= 0

        return max(maxOnes, aux)