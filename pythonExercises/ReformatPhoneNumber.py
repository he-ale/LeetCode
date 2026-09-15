class Solution:
    def reformatNumber(self, number: str) -> str:
        phoneNumber= ""
        aux= ""
        for n in number:
            if (n.isdigit()):
                aux+= n
                if (len(aux) == 3):
                    phoneNumber+= aux+ "-"
                    aux= ""
        if (aux == ""):
            return phoneNumber[:-1]
        elif (len(aux) == 1):
            return phoneNumber[:-1] + "-" + phoneNumber[-1] + aux
        else:
            return phoneNumber + "-" + aux