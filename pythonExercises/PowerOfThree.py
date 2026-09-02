class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (3 > n and n != 1):
            return False
        
        aux= abs(n)

        while (aux % 3 == 0 ):
            aux//= 3
        
        return aux == 1