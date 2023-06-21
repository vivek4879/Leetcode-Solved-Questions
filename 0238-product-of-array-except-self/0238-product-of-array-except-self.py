class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = 1
        pps = 1
        res=[]
        presum =[1]
        postsum=[1]
        for i in range(len(nums)-1):
            ps = ps * nums[i]
            presum.append(ps)
        for i in range(-1, -(len(nums)), -1):
            pps = pps * nums[i]
            postsum.append(pps)
        
        postsum=postsum[::-1]
        
        for i in range(len(nums)):
            res.append(presum[i] * postsum[i])
            
        return res
            