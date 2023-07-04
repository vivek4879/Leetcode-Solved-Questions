class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #stack to track speeds
        new = [[p,s] for p,s in zip(position,speed)] #this array will hold all the position and speed pairs of each car. This array is made using python list composition
        
        for p , s in sorted(new)[::-1]: #looping through the sorted reversed list
            time = (target - p) / s     #finding time for each car to reach the target from its current position
            if stack and stack[-1] < time:   # if stack not empty and the time at top of stack is less than time for current car then we append new time
                stack.append(time)
            elif stack and stack[-1] >= time:   #if stack not empty and speed at top of stackgreater than or equal to the time for current car then we continue to next car
                continue
            else:                      #if stack empty then we append the speed to the stack
                stack.append(time)
        return len(stack)