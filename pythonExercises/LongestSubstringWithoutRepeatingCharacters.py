class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary= dict()
        ini= 0
        maxLen= 0
        for i in range(len(s)):
            if s[i] in dictionary and dictionary[s[i]] >= ini:
                ini = dictionary[s[i]] + 1

            dictionary[s[i]] = i
            maxLen = max(maxLen, i - ini + 1)
        return maxLen