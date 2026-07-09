class Solution:
    def countSegments(self, s: str) -> int:
        if(s.isspace()):
            return 0
        xs= s.split(" ")

        counter= 0
        for x in xs:
            if(x!=""):
                counter+=1
        return counter