class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        val_count = 0
        under_val = 0
        
        for i in nums:
            if i == target:
                val_count+=1
            if i < target:
                under_val+=1
        
        return(i for i in range(under_val, under_val+val_count))