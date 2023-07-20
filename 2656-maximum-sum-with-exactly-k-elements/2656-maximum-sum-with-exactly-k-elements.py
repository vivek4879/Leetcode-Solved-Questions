class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_n = nums[-1]
        max_sum = 0
        while k > 0:
            max_sum = max_sum + max_n
            max_n +=1
            k-=1
        return max_sum
            