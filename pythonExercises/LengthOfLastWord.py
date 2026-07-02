class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i= len(s)-1
        while(i>=0 and s[i]==' '):
            i-=1
        
        lenght= 0
        while(i>=0 and s[i]!=' '):
            i-=1
            lenght+=1
        return lenght