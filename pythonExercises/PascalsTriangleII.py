from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if (rowIndex == 0):
            return [1]
        elif (rowIndex == 1):
            return [1,1]
        row= [1, 1]
        aux= [1]
        for i in range(2, rowIndex+1):
            for i in range(1, len(row)):
                aux.append(row[i]+row[i-1])
            aux.append(1)
            row= aux
            aux= [1]
        return row 