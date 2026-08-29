from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words= dict()
        paragraph= re.findall(r'[a-z]+',paragraph.lower())
        for e in paragraph:
            if e not in banned:
                if e in words:
                    words[e]+= 1
                else:
                    words[e]= 1

        result= ''
        occurrences= 0

        for key, value in words.items():
            if value > occurrences:
                result= key
                occurrences= value

        return result

s= Solution()
s.mostCommonWord("Bob", [])