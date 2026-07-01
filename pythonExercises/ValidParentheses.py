from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack= deque()
        for e in s:
            if e in "({[":
                stack.append(e)
            else:
                if not stack:
                    return False
                a= stack.pop()
                if ('('!=a and e==')'):
                    return False
                elif ('['!=a and e==']'):
                    return False
                elif ('{'!=a and e=='}'):
                    return False
                
        return len(stack)==0
    
s= Solution()

print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
print(s.isValid("([)]"))
print(s.isValid("({[)"))

                    

