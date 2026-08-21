from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        d= datetime.strptime(date, "%Y-%m-%d")
        return int(d.strftime("%j"))

s= Solution()
print(s.dayOfYear("2019-02-10"))