from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        xs= []
        for i in range(1, n+1):
            if (i % 15 == 0):
                xs.append("FizzBuzz")
            elif (i % 3 == 0 ):
                xs.append("Fizz")
            elif (i % 5 == 0):
                xs.append("Buzz")
            else:
                xs.append(str(i))
            
        return xs