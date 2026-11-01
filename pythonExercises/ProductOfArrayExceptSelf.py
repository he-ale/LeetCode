class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        j= len(nums)-1
        l= [1]
        r= [1]
        for i in range(len(nums)-1):
            l.append(l[i]*nums[i])
            r.append(r[i]*nums[j])
            j-=1

        result=[]
        k= len(nums)-1
        for i in range(len(nums)):
            result.append(l[i]*r[k])
            k-=1

        return result