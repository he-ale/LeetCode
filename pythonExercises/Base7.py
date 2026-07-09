class Solution:
    def convertToBase7(self, num: int) -> str:
        rs=""
        negative= False
        if num<0:
            negative= True
            num= abs(num)
        while (num>6):
            rs+=str(num%7)
            num//=7
        rs= rs+str(num)
        return "-"+rs[::-1] if negative else rs[::-1]