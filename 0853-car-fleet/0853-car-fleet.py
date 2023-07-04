class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        new = [[p,s] for p,s in zip(position,speed)]
        
        for p , s in sorted(new)[::-1]:
            time = (target - p) / s
            if stack and stack[-1] < time:
                stack.append(time)
            elif stack and stack[-1] >= time:
                continue
    
            else:
                stack.append(time)
        return len(stack)