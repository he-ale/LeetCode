from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen= len(strs[0])
        index= 0
        for i in range(1,len(strs)):
            if minLen>len(strs[i]):
                minLen= len(strs[i])
                index= i

        result= ""

        for i in range(minLen):
            for elem in strs:
                if(strs[index][i]!=elem[i]):
                    return result
            result= result+strs[index][i]
        
        return result

solution= Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
