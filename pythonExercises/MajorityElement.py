from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies= {}
        for num in nums:
            if frequencies.get(num):
                frequencies[num]+=1
            else:
                frequencies[num]=1

        res= 0
        aux= 0
        for k, v in frequencies.items():
            if (aux < v):
                res= k
                aux= v
        return res
