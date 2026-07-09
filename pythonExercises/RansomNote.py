class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ls= set(ransomNote)
        for e in ls:
            if magazine.count(e)-ransomNote.count(e)<0:
                return False
        return True
