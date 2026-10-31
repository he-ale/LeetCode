from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= {}
        for word in strs:
            key= [0]*26
            for w in word:
                key[ord(w)-ord('a')]+= 1
            key= '#'.join(key)
            if key not in groups:
                groups[key]= []
            groups[key].append(word)
        
        return list(groups.values())
    

