
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)   
        INT_MAX = 2**31 - 1

        s=s.strip()
        i = 0
        number= 0
        isNegative= False
        if s=='':
            return 0

        if s[0]=='-':
            i=1
            isNegative= True
            
        if s[0]=='+':
            i=1

        for c in s[i:]:
            if( not c.isnumeric()):
                break
            number= (number*10)+int(c) 

        return max(INT_MIN, -number) if isNegative else min(number, INT_MAX)
    

