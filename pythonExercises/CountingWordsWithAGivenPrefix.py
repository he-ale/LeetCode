class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        counter= 0
        for word in words:
            if word.startswith(pref):
                counter+=1
        return counter