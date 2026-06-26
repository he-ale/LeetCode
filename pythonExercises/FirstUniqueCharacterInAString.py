class Solution:
    def firstUniqChar(self, s: str) -> int:
        m= {}
        for l in s: 
            if m.get(l):
                m[l]= m[l]+1
            else:
                m[l]=1
        
        for i in range(len((s))):
            if(m[i]==1):
                return i 

        return -1