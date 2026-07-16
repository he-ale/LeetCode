class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        j= 0
        for e in t:
            if(e == s[j]):
                j+=1
            if(j == len(s)):
                return True
    
        return False