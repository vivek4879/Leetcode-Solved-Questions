class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {} 
        freq = [[] for i in range(len(nums) +1)]
        
        # creating a dictionary which has counts of each element of nums
        for i in nums: 
            count_dict[i] = 1 + count_dict.get(i, 0)
        
        #creating a list of lists with each list consisting elements which have  frequency equal to the index of that list.
        for i,j in count_dict.items(): 
            freq[j].append(i)
            
        #creating result array
        res=[]
        
        #here we go through the freq aray in reverse order hence starting from end of array and going till zero as we want to return the most frequent elements.
        for i in range(len(freq) - 1, 0 , -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
