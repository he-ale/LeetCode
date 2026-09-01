from typing import List

class Solution:
    def valid(self, s:  List[str]) -> bool:
        return  s[::-1] == s

    def validPalindrome(self, s: List[str]) -> bool:
        if s[::-1] == s:
            return True
        return self.__validPalindrome__(list(s))

    def __validPalindrome__(self, letters: List[str]):
        i= 0
        j= len(letters)-1
        while (i <= j):
            if(letters[i] != letters[j]):
                break
            i+= 1
            j-= 1
        a= letters[:i]+letters[i+1:]
        b= letters[:j]+letters[j+1:]
        return self.valid(a) or self.valid(b)
    