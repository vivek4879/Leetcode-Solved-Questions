class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = 1
        pss = 1
        res=[1]
        
        #calculating prefix(product of all elements before the one in consideration) and storing in the result array
        
        for i in range(len(nums)-1):
            ps=ps*nums[i]
            res.append(ps)
        
        #calculating postfix(product of all elements after the one in consideration) and then multiplying it with the prefixes already stored in res arrray. This way we only need one res array.
        
        
        for i in range(-1, -(len(nums)+1), -1):
            res[i]= res[i] * pss
            pss= pss * nums[i]
        return res
            
                    