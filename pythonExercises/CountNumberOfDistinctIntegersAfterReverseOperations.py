from typing import List

class Solution:

    def __reverseInt__(self, num: int):
        n= 0
        while(num>0):
            n= (n*10)+(num%10)
            num//=10
        return n        

    def countDistinctIntegers(self, nums: List[int]) -> int:
        # s= set(nums)
        # for num in nums:
        #     n= self.__reverseInt__(num)
        #     s.add(n)
        
        # return len(s)
        s= set(nums)
        for num in nums:
            n= int(str(num)[::-1])
            s.add(n)
        return len(s)
    
s= Solution()

print(s.countDistinctIntegers([1,13,10,12,31]))
