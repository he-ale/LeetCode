class Solution:
    INT_MIN = -(2**31)   
    INT_MAX = 2**31 - 1

    def reverse(self, x: int) -> int:    
        number= 0
        isNegative= False
        
        if x<0:
            isNegative= True
            x= abs(x)

        while (x > 0):
            number= (number*10) + (x%10)
            x//= 10

        if isNegative:
            number= -number

        if number < Solution.INT_MIN:
            return 0
        if number >Solution.INT_MAX:
            return 0
        return number