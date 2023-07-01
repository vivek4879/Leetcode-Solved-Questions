class Solution:
    def trap(self, height: List[int]) -> int:
        finalhold = 0
        l , r = 0 , len(height)-1
        leftmax , rightmax = height[l],height[r]
        
        while l < r:
            if leftmax < rightmax:
                l +=1
                leftmax = max(leftmax, height[l])
                finalhold += leftmax - height[l]
            else:
                r-=1
                rightmax = max(rightmax,height[r])
                finalhold += rightmax - height[r]          
            
        return finalhold
            