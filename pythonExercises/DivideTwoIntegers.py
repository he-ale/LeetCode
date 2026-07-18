class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result= int(dividend/divisor)
        if (-2147483648 > result ):
            return -2147483648
        elif ( result > 2147483647):
            return 2147483647
        return result