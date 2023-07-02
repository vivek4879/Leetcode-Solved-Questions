class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentdict = {')' : '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in parentdict:
                if stack and parentdict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False
                
            