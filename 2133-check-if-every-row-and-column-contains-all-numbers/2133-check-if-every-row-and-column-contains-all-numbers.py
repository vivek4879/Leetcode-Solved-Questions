class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row = collections.defaultdict(set)
        cols=collections.defaultdict(set)
        res = [i+1 for i in range(len(matrix))]
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] not in row[i] or matrix[i][j] not in cols[j]:
                    row[i].add(matrix[i][j])
                    cols[j].add(matrix[i][j])
    
                    
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if res[i] not in row[j] or res[i] not in cols[j]:
                    return False
        return True
            