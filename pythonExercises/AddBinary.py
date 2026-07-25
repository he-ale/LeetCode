class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a= a[::-1]
        b= b[::-1]
        i= 0
        j= 0
        carry= 0
        result=[]
        while (i<len(a) and j<len(b)):
            aux= int(a[i])+int(b[j])+carry

            if (aux < 2):
                carry= 0
                result.append(str(aux))
            elif (aux == 2):
                carry=1
                result.append("0")
            else:
                carry=1
                result.append("1")
            i+=1
            j+=1

        while (i<len(a)):
            aux= int(a[i])+carry

            if (aux < 2):
                carry= 0
                result.append(str(aux))
            else:
                carry=1
                result.append("0")
            
            i+=1
        while (j<len(b)):
            aux= int(b[j])+carry

            if (aux < 2):
                carry= 0
                result.append(str(aux))
            else:
                carry=1
                result.append("0")
            
            j+=1
        if carry:
            result.append("1")
        result= result[::-1]
        return "".join(result) 
        