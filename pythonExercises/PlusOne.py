from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry= True
        for i in range(len(digits)-1, -1, -1):
            if carry:
                digits[i]+=1
            if (digits[i]>9):
                carry= True
                digits[i]%=10
            else:
                carry= False
                return digits
        if carry:
            digits= [1]+digits
        return digits