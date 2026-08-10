class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rs= 0
        for e in columnTitle:
            rs= rs * 26 + (ord(e) - ord("A") + 1)
        return rs