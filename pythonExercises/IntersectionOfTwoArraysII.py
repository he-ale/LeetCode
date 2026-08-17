from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictn1: dict= {}
        dictn2: dict= {}
        n: int= max(len(nums1), len(nums2))
        for i in range(n):
            if(i < len(nums1)):
                if dictn1.get(nums1[i]):
                    dictn1[nums1[i]]+= 1
                else:
                    dictn1[nums1[i]]= 1
            if(i < len(nums2)):
                if dictn2.get(nums2[i]):
                    dictn2[nums2[i]]+= 1
                else:
                    dictn2[nums2[i]]= 1
        nums= list(set(nums1))
        rs= []
        for e in nums:
            if dictn1.get(e) and dictn2.get(e):
                rs=rs + [e]*min(dictn1[e], dictn2[e])
        return rs

s= Solution()
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))