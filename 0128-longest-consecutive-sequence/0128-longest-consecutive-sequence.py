class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = set(nums)
        maxs = 0
        x=0
        for i in nums:
            if i-1 not in nums1:
                x = 1
                while i+1 in nums1:
                    x+=1
                    i = i+1   
                maxs = max(maxs, x)
        return maxs
                