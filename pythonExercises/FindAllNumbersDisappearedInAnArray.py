class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        mySet= set(nums)
        result= []
        for i in range(1, len(nums)+1):
            if i not in mySet:
                result.append(i)
        return result