from typing import List

class Solution:
    

    def search(self, nums: List[int], target: int) -> int:
        right= len(nums)-1
        left= 0
        while (left<=right):
            mid= (left+right)//2
            if(nums[mid] == target):
                return mid

            if(nums[left]<nums[right]):
                if(target<nums[mid]):
                    right= mid-1
                else:
                    left= mid+1
            else:
                if target<nums[mid] or target>=nums[left]:
                    right= mid-1
                elif target>nums[mid] and target<=nums[left]:
                    left= mid+1
                elif target<nums[mid] and target>=nums[left]:
                    right= mid-1
                elif target<nums[mid] and target<nums[right]:
                    left=mid+1