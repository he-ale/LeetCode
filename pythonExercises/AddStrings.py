class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num= ""
        i= len(num1)-1
        j= len(num2)-1
        flag= False

        while(i > -1 and j > -1):
            aux= ord(num1[i]) + ord(num2[j]) - 96 + flag

            if aux>9:
                aux= str(aux)[-1]
                flag= True
            else:
                aux= str(aux)
                flag= False
            num= aux + num
            i-=1
            j-=1
        
        while(i > -1):
            aux= ord(num1[i]) - 48 + flag
            if aux>9:
                aux= str(aux)[-1]
                flag= True
            else:
                aux= str(aux)
                flag= False
            num= aux + num
            i-=1
        
        while(j > -1):
            aux= ord(num2[j]) - 48 + flag
            if aux>9:
                aux= str(aux)[-1]
                flag= True
            else:
                aux= str(aux)
                flag= False
            num= aux + num
            j-=1

        return "1"+num if flag else num

s= Solution()
print(s.addStrings("456","77"))