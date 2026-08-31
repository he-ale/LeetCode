from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result= [[] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j].append(matrix[i][j])
        return result

s= Solution()
print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))
            