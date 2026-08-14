class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionaryP= dict()
        dictionaryS= dict()
        s= s.split(" ")
        if (len(pattern) != len(s)):
            return False
        for i in range(len(s)):
            if (dictionaryP.get(pattern[i]) and dictionaryS.get(s[i])):
                if (dictionaryP[pattern[i]] != dictionaryS[s[i]]):
                    return False
            elif ((not dictionaryP.get(pattern[i])) and dictionaryS.get(s[i])):
                return False
            elif (dictionaryP.get(pattern[i]) and (not dictionaryS.get(s[i]))):
                return False
            else:
                dictionaryP[pattern[i]]= i+1
                dictionaryS[s[i]]= i+1
        return True
