class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0, len(s)-k+2, k):
            j=i
            l=min(i+k-1, len(s)-1)
            while (j<l):
                s[j], s[l]= s[l],s[j]
                j+=1
                l-=1
        return "".join(s)
        
s= Solution()
print(s.reverseStr("abcdefg",2))
