class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        res = []
        res1=[]
        for i in nums:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] = mydict[i] + 1
        sorted_dict = sorted(mydict.items(), key=lambda x: x[1], reverse = True)
        for i,j in sorted_dict:
            res.append (i)

        for i in range(k):
            res1.append(res[i])
        return res1
