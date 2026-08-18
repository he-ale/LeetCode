from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums= list(set(nums))
        # nums.sort(reverse= True)
        # if (len(nums) > 2):
        #     return nums[2]
        # return nums[0]
        first= second= third= None
        for num in nums:
            if (first == num or second == num or third == num):
                continue

            if (first is None or num > first):
                third= second
                second= first
                first= num
            elif (second is None or num > second):
                third= second
                second= num
            elif (third is None or num > third):
                third= num

        return first if third is None else third

s= Solution()
print(s.thirdMax([2,2,3,1])) 

