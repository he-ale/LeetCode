
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        aux= {}
        aux2= {}
        for i in range(len(s)):
            if s[i] not in aux:
               aux[s[i]]= i
            if t[i] not in aux2:
               aux2[t[i]]= i
            if(aux2[t[i]]!=aux[s[i]]): 
                return False
        return True