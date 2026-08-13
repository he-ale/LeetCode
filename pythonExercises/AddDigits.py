class Solution:
    def addDigits(self, num: int) -> int:
        rs= 0
        while (num >= 10):
            while (num > 9):
                rs+= num%10
                num = num//10
            num= rs+num
            rs= 0
        return rs