class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result= [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i]+result[i-1])
        return result