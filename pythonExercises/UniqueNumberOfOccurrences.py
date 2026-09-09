from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary= dict()
        for e in arr:
            if e in dictionary:
                dictionary[e]+= 1
            else:
                dictionary[e]= 1
        return len(dictionary) == len(set(dictionary.values()))
        