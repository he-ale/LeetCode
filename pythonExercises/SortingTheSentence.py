class Solution:
    def sortSentence(self, s: str) -> str:
        xs= s.split(" ")
        dictionary= { int(e[-1]): e[:-1] for e in xs }
        result= ""
        for i in range(len(xs)):
            result= f"{result} {dictionary[i+1]}"
        return result[1:]