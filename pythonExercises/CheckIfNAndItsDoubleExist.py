class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        dicctionary= {}
        for e in arr:
            if e in dicctionary:
                return True
            if (e%2 == 0) and (e//2) not in dicctionary:
                dicctionary[e//2]= e
            if (e*2) not in dicctionary:
                dicctionary[e*2]= e
            
        return False