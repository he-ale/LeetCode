class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters= {'b','a','l','o','n'}
        xs=[]
        for l in letters:
            if (l == 'l' or l == 'o'):
                xs.append(text.count(l)//2)
            else:
                xs.append(text.count(l))
        return 0 if len(xs)<5 else min(xs)

s= Solution()
s.maxNumberOfBalloons("loonbalxballpoon")