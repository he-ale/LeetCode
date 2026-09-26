class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        if len(nums)==1:
            return [nums[0]**2]
        left=self.sortedSquares(nums[:len(nums)//2])
        right=self.sortedSquares(nums[len(nums)//2:])

        return self._mergue(left, right)

    def _mergue(self, left, right):
        i= 0
        j= 0
        listSorted= []
        while (i< len(left) and j < len(right)):
            if(left[i] < right[j]):
                listSorted.append(left[i])
                i+= 1
            else:
                listSorted.append(right[j])
                j+= 1

        while(i< len(left)):
            listSorted.append(left[i])
            i+= 1
        while(j< len(right)):
            listSorted.append(right[j])
            j+= 1

        return listSorted