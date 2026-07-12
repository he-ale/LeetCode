class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rs=''
        for i in range(0, len(s), 2*k):
            rs+= s[i:i+k][::-1]
            rs+= s[i+k, i+2*k]
        return rs
        
