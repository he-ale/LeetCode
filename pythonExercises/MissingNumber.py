class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        dictionary= {}
        for num in nums:
            dictionary[num]= 1

        i, j= 0, len(nums)
        while (i <= j):
            if i not in dictionary:
                return i
            elif j not in dictionary:
                return j
            i+= 1
            j-= 1