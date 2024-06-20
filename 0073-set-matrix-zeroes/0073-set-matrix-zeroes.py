class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        rows_to_zero = set()
        cols_to_zero = set()
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)                
                    
        for i in rows_to_zero:
                self.set_row_to_zero(i, matrix)

        for j in cols_to_zero:
                self.set_col_to_zero(j, matrix)
            
            
    def set_row_to_zero(self, row_idx: int, matrix: List[List[int]]) -> None:
        cols = len(matrix[0])
        for j in range(cols):
            matrix[row_idx][j] = 0
    
    def set_col_to_zero(self, col_idx: int, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        for i in range(rows):
            matrix[i][col_idx] = 0         
        
        