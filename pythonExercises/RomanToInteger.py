class Solution:
    
    __dictionary__= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        current= s[0]
        result= self.__dictionary__[current]
        s=s[1:]
        for e in s:
            if(e == current):
                result+= self.__dictionary__[e]
            else:
                if (self.__dictionary__[current]<self.__dictionary__[e]):
                    result-=self.__dictionary__[current]
                    result= result+self.__dictionary__[e]-self.__dictionary__[current]
                else:
                    result+=self.__dictionary__[e]
            current= e
        return result
    
s= Solution()
print(s.romanToInt("XLIV"))