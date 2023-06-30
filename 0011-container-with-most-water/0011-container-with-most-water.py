class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r, maxarea = 0, len(height) -1, 0
    
        while l < r:
            area = (r-l) * min(height[r],height[l])
            maxarea=max(maxarea,area)
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        return maxarea
                
                    
                
            
            