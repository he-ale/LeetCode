class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        xs= s.split(" ")
        lastNumber = -1
        for x in xs:
            if x.isdigit():
                if lastNumber >= int(x):
                    return False
                else:
                    lastNumber= int(x)
        return True