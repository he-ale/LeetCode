class Solution:
    def isHappy(self, n: int) -> bool:
        register= set()
        while (n != 1):
            if n in register:
                return False
            register.add(n)
            aux= 0
            while (n > 0):
                aux+= (n%10)**2
                n//=10
            n= aux
        return True