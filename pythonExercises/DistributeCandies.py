class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        mySet= len(set(candyType))
        aux= len(candyType)//2
        if (mySet<aux):
            return mySet
        return aux