class MinStack:

    def __init__(self):
        #we initiate 2 stacks, one to store the pushed values so that we can get the top element when needed, and other to store the minimum element at each iteration.
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        #we use append function to push the values in our stack
        self.stack.append(val)
        #to push values in our minstack, we first check if the current value pushed is less than the element already at the top of the stack and append whichever is less at that point
        if self.minstack:
            val= min(val,self.minstack[-1])
        self.minstack.append(val)
            
        #we use pop function to remove the top element in both our stacks.
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()