from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if (numRows == 1):
            return [[1]]
        if (numRows == 2):
            return [[1], [1,1]]

        
        result= [[1], [1,1]]
        for j in range(2, numRows):
            aux= [1]
            for k in range(1, len(result[j-1])):
                aux.append(result[j-1][k-1]+result[j-1][k])
            aux.append(1)
            result.append(aux)
        return result