from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        total= len(mat)*len(mat[0])
        if (total != r*c or (len(mat)== r and len(mat[0]) == c)):
            return mat

        result= []
        aux= []
        for j in range(len(mat)):
            for i in range(len((mat[0]))):
                aux.append(mat[j][i])
                if (len(aux) == c):
                    result.append(aux)
                    aux= []
                
        return result