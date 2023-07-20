class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_n = nums[-1]
        ans = 0
        for i in range(max_n, max_n + k):
            ans = ans + i
        return ans