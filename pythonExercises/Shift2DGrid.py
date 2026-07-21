from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n= len(grid)
        m= len(grid[0])
        xs= []
        for ls in grid:
            for e in ls:
                xs.append(e)
        i= k% (n*m)
        xs= xs[(m*n)-i:]+xs[:(m*n)-i]
        for j in range(n):
            grid[j]= xs[j*m:(j*m)+m]
        return grid

