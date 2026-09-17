class Solution:
    def longestPalindrome(self, s: str) -> int:
        dicctionary= {}
        for e in s:
            if e in dicctionary:
                dicctionary[e]+= 1
            else:
                dicctionary[e]= 1
        evenSum= 0
        oddSum= 0
        for value in dicctionary.values(): 
            if (value%2 == 0):
                evenSum+= value
            else:
                if (value > 1):
                    evenSum+= value-1
                    oddSum+= 1
                else:
                    oddSum+=1

        if (oddSum > 0):
            return 1 + evenSum
        elif (evenSum == 0):
            return 1
        else:
            return evenSum

                