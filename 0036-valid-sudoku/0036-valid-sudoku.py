class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #creating dictionaries of sets by defaultdict  so that even if there is no key, it will get generated. also using set as the argument as we would like to create sets for earch row, column, and square.
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares= collections.defaultdict(set)
        #iterating over the range 9 as it is given the size will be 9X9 only.
        for i in range(9):
            for j in range(9):
                # passing over any "." in the sudoku
                if board[i][j] == ".":
                    continue
                #here we check if the element in consideration is already present in our dictionaries. If it already exists then we return false
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3,j//3)]:
                    return False
                #here we add the element in consideration to the respective set in the row, column and square dictionary.
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3),(j//3)].add(board[i][j])
        #we return True in case we reach here as it means there were no duplicates        
        return True
                    
                
        