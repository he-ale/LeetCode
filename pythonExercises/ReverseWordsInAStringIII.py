class Solution:
    def reverseWords(self, s: str) -> str:
        xs= s.split(" ")
        for i in range(len(xs)):
            xs[i]=xs[i][::-1]

        return " ".join(xs)
    
solution= Solution()

print(solution.reverseWords("Let's take LeetCode contest"))