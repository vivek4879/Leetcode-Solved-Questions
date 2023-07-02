class Solution:
    def isValid(self, s: str) -> bool:
        #we create a stack which will store opening parentheses if we encounter one in our loop
        stack = []
        #we create a hashmap in whihc we store all the closing parentheses as keys
        parentdict = {')' : '(', ']': '[', '}': '{'}
        
        #iterating through the input string s
        for i in s:
        #we check if i is a clsoing parenthesis by checking if its in out dict or not. if it is not in our dict, its an opening parenthesis and we then add it to our stack. If its a closing parenthesis then we further check if its opening counterpart is at the top of our stack, if it is, we just remove it from top of stack and carry on, if it is not then we return false. 
            if i in parentdict:
                if stack and parentdict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
       #we return true is our stack is empty in the end as that means all opening parentheses has closings too.         
        return True if not stack else False
                
            