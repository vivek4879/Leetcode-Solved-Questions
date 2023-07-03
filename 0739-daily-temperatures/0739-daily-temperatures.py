class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #first we initiate an array of lenght equal to the input temperature array with all elements as zero because if we dont find temperatures greater than the one in question then we need zero.
        res = [0] * len(temperatures)
        #we will use a stack to keep note of the temperatures
        stack=[]
        #we iterate through temperatures using enumerate as we need indexes too.
        for i , n in enumerate(temperatures):
            #while our stack has a top element we see if the temp in question is greater than the stack top temp, if it is, then we insert at the index of the stacks top element in the res array the difference between the index in iteration and the index of the top of the stack temp. then we pop the top of the stack.
            while stack and n > stack[-1][0]:
                res[stack[-1][-1]] = i - stack[-1][-1]
                stackT, stackI = stack.pop()    
            stack.append([n , i])
        return res
            