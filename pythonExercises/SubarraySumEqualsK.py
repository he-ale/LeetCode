from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        register= {0: 1}
        cs= 0
        counter= 0
        for num in nums:
            cs+=num
            c= cs-k
            counter+= register.get(c,0)
            register[cs]= register.get(cs, 0)+1

        return counter