class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mydict = {')': '('}
        stack = []
        x = 0
        
        for i in s:
            if stack and i in mydict:
                if stack[-1] == mydict[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        return (len(stack))