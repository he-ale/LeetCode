import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= re.sub(r'[^a-zA-Z0-9]', '', s)
        s= s.lower()
        i= 0
        j= len(s)-1

        while (i<j):
            if( s[i]!=s[j] ):
                return False
            i+=1
            j-=1
        return True
    
solution= Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))
print(solution.isPalindrome('race a car'))
print(solution.isPalindrome(' '))
                
            