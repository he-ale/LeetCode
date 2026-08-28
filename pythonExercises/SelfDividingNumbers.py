from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numberList= []
        for num in range(left, right+1):
            if (num % 10 != 0):
                if self.__isDividedByItself__(num):
                    numberList.append(num)
        return numberList

    def __isDividedByItself__(self, num: int):
        index= num
        while (index > 0):
            aux= index % 10
            if (aux == 0 or num % aux != 0):
                return False
            index= index//10
        return True