import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        limit= int(math.sqrt(num)) + 1
        rs= 0
        i= 1
        for i in range(1, limit):
            if (num%i == 0):
                rs+= i
                aux= num//i
                if (aux != num and i != aux):
                    rs+= aux
        return rs==num