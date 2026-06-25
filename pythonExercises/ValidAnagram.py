
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        sequence= set(s)

        for e in sequence:
            if s.count(e)!=t.count(e):
                return False

        return True
    
solution= Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
