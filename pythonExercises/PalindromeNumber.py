class Solution:
    def isPalindrome(self, x: int) -> bool:
        number= str(x)
        i= 0
        j= len(number)-1
        while (i<j):
            if(number[i]!=number[j]):
                return False
            i+=1
            j-=1
        return True
    
    def isPalindromeV2(self, x: int) -> bool:
        number= str(x)
        return number[::1]==number
