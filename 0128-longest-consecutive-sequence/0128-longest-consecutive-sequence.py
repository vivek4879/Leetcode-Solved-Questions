class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = set(nums)
        maxs = 0
        
        
        for i in nums:
            #checking for every element in nums if its. preceding element is also in nums. If it has a preceding element in nums then it is not the start of a sequence. if it is start of a sequence then we move ahead.
            if i-1 not in nums1:
                seq = 0
                #as long as we find succeding consecutive elements in nums, we keep adding one to the seq and then compare current seq with the maxs
                while i+seq in nums1:
                    seq+=1
                maxs = max(maxs, seq)
        return maxs
                