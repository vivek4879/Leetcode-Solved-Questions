class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        new = [[p,s] for p,s in zip(position,speed)] 
        for p , s in sorted(new)[::-1]: 
            stack.append((target - p) / s)     
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)