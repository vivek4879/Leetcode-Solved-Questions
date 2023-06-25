class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #we initiate two pointers m and n, one starting from start and other from the end
        m,n = 0, len(numbers)-1
        #we enter a while loop until the pointers meet
        while m <= n:
        #we get the sum of the elements at the two pointer positions
            sum1 = numbers[m] + numbers[n]
        #first we check if the two elements add up to the target and return the endices if they do.
            if sum1 == target:
                return([m+1,n+1])
        # if the two indices dont sum up to the target then we check if the sum is greater than the target, if it is, then we update the last counter to one less and keep the first counter as it is.
            elif sum1 > target:
                n = n -1
        #if the sum is less than the target then we keep the last counter as is and increment the first counter
            else:
                m +=1
            
            