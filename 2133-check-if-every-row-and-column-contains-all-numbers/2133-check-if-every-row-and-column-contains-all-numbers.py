class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        #created defaultdicts 
        row = collections.defaultdict(set)
        cols=collections.defaultdict(set)
        
        #creating a array of all the integers from 1 to n.
        res = [i+1 for i in range(len(matrix))]
        
        
        #adding all the elements present in the matrix in the defaultdict sets for each column and row
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] not in row[i] or matrix[i][j] not in cols[j]:
                    row[i].add(matrix[i][j])
                    cols[j].add(matrix[i][j])
    
        # checking if each integer in res is also present in the defaultdict sets or not. We return false if even one is not present, else we return true in the end.            
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if res[i] not in row[j] or res[i] not in cols[j]:
                    return False
        return True
            