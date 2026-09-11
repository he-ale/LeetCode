class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        limit= max(len(word1), len(word2))
        i= 0
        word= ""
        while (i < limit):
            if (i < len(word1)):
                word+= word1[i]
            if (i < len(word2)):
                word+= word2[i]
            i+= 1
        return word