class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = 1
        pss = 1
        res=[1]

        for i in range(len(nums)-1):
            ps=ps*nums[i]
            res.append(ps)
        
        for i in range(-1, -(len(nums)+1), -1):
            res[i]= res[i] * pss
            pss= pss * nums[i]
        return res
            
                    