from typing import List

class Solution:
    def __binarySearch__(self, nums: List[int], target: int)->int:
        i= 0
        j= len(nums)-1
        while (i <= j):
            k= (i+j)//2
            if nums[k]==target:
                return k

            elif nums[k]<target:
                i= k+1
            else:
                j= k-1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<=3:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i

        b= [nums[0]]
        k= len(nums)
        for i in range(1, len(nums)):
            if(b[-1]<nums[i]):
                b.append(nums[i])
                k-=1
            else:
                break
        print(b)
        result= self.__binarySearch__(b, target)
        if result!=-1:
            return result
        
        a= nums[-k+1:]
        print(a)
        result= self.__binarySearch__(a, target)
        return len(nums)-k+result+1 if result!=-1 else result

