class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out=[]
        nums.sort()
        
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            g,h = i+1 , len(nums) - 1
            while g < h:
                sum1 = nums[g] + nums[h] + n
                
                if sum1 > 0:
                    h = h - 1
                elif sum1 < 0:
                    g = g + 1
                else:
                    out.append([nums[g],nums[h],n])
                    g +=1
                    while nums[g] == nums[g-1] and g < h:
                        g+=1
        return (out)
                    
                
    
                
                