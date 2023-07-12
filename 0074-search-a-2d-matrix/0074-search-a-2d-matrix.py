class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
            
        
        L,R = 0, len(matrix) - 1
        while L <= R:
            mid = (L+R) // 2
            if target < matrix[mid][0]:
                R = mid - 1
            elif target > matrix[mid][-1]:
                L = mid + 1
            else:
                mat = matrix[mid]
                break
        if not (L<= R):
            return False
        else:
            l,r = 0, len(mat)-1
            while l <= r:
                mid = (l+r)//2
                if target < mat[mid]:
                    r = mid - 1
                elif target > mat[mid]:
                    l = mid + 1
                else:
                    return True
            return False
    
        
            