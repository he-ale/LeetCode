class Solution:
    def __init__(self):
        self.code = {i: chr(64 + i) for i in range(1, 27)}

    def convertToTitle(self, columnNumber: int) -> str:
        rs= ''
        while(columnNumber>26):
            index= columnNumber%26
            columnNumber//=26
            if index==0:
                rs= self.code[26]+rs
                columnNumber-=1
            else:
                rs= self.code[index]+rs
        return self.code[columnNumber]+rs