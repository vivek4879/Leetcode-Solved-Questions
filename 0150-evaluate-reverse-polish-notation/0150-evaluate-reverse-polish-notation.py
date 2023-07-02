class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                x= stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(x)       
            elif i == "-":
                x= stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(x)
            elif i == "*":
                x= stack[-1]*stack[-2]
                stack.pop()
                stack.pop()
                stack.append(x)
            elif i == "/":
                x= stack[-2]/stack[-1]
                stack.pop()
                stack.pop()
                stack.append((int(x)))
            else:
                stack.append(int(i))
        return stack[-1]
        
                