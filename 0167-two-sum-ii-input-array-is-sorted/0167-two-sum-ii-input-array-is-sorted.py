class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m,n = 0, len(numbers)-1
        
        while m <= n:
            sum1 = numbers[m] + numbers[n]
            if sum1 == target:
                return([m+1,n+1])
            elif sum1 > target:
                n = n -1
            else:
                m +=1
            