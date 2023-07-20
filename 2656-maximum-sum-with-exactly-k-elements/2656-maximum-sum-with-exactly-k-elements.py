class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_num = 0
        for i in range(k):
            max1 = nums[-1]
            max_num = max_num + max1
            nums[-1] = max1 + 1
        return max_num
            