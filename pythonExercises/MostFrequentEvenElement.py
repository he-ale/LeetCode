from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        frequencies= {}
        for num in nums:
            if (num % 2 == 0):
                if (frequencies.get(num)):
                    frequencies[num]+=1
                else:
                    frequencies[num]= 1

        minNum= -1
        rep= 0
        for key, value in frequencies.items():
            if (value > rep):
                minNum= key
                rep= value
            elif (value == rep):
                minNum= min(minNum, key)

        return minNum