class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        dictionary= {}
        for num in nums:
            if num not in dictionary:
                dictionary[num]= 1
            else:
                dictionary[num]+= 1
        for value in dictionary.values():
            if (value%2 != 0):
                return False

        return True