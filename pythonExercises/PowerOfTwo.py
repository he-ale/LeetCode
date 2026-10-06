class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        aux= 1
        while (n > aux):
            aux=aux<<1

        return n==aux