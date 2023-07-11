class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[]
        left_smaller = []
        right_smaller = []
        max_area = 0
        
        for i, n in enumerate(heights):
            if not stack:
                left_smaller.append(0)
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= n:
                    stack.pop()
                if stack:
                    left_smaller.append(stack[-1]+1)
                    stack.append(i)
                else:
                    left_smaller.append(0)
                    stack.append(i)
        stack =[]
        for i ,n in reversed(list(enumerate(heights))):
            if not stack:
                right_smaller.append(i)
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= n:
                    stack.pop()
                if stack:
                    right_smaller.append(stack[-1]-1)
                    stack.append(i)
                else:
                    right_smaller.append(len(heights)-1)
                    stack.append(i)
                
        right_smaller=(right_smaller[::-1])
        print(left_smaller)
        print(right_smaller)
        
        for i, n in enumerate(heights):
            area = ((abs(left_smaller[i]-right_smaller[i]) + 1) * n )
            
            if area > max_area:
                max_area = area
                
        return max_area
            
                    
                    
                
                