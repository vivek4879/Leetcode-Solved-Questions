class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res=[]
        res1=[]
        res2=[]
        for i in nums:
            if i < pivot:
                res.append(i)
            if i > pivot:
                res1.append(i)
            if i == pivot:
                res2.append(i)
        return(res+res2+res1)