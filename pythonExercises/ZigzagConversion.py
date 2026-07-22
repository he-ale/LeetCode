class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix= ["" for k in range(numRows)]
        j= 0
        direction= 1
        for e in s:
            matrix[j]+=e
            
            if(j == numRows-1):
                direction= -1
            if(j == 0):
                direction= 1
            j+= direction
        return "".join(["".join(xs) for xs in matrix])

s= Solution()
print(s.convert("PAYPALISHIRING", 3))