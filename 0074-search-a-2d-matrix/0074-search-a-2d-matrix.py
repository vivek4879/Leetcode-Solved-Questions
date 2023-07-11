class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        def lin_search(arr):
            l,r = 0, len(arr)-1
            while l <= r:
                mid = (l+r)//2
                if target < arr[mid]:
                    r = mid - 1
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    return True
            return False
        
        for i in matrix:
            if lin_search(i) == True:
                return True
        return False