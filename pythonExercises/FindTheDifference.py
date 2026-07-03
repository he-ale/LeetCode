
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for ch in s:
            x ^= ord(ch)
        for i in t:
            x ^= ord(i)
        return chr(x)