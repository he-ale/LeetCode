class Solution:
    def checkString(self, s: str) -> bool:
        s= list(s)
        a= sorted(s)
        return a==s
