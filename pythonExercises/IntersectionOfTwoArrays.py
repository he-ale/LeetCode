from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # a= list(set(nums1))
        # b= list(set(nums2))
        # if (len(a) > len(b)):
        #     a, b= b, a
        # ls= []
        # for e in a:
        #     if e in b:
        #         ls.append(e)
        # return ls
        return list(set(nums1)&set(nums2))
        
        