class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = (len(matrix) * (len(matrix[0])) - 1) # rows * columns
        
        while low <= high:
            center = (low + high) // 2 # center of matrix
            row, column = divmod(center, len(matrix[0])) # get row and column

            if matrix[row][column] == target: # if value = target
                return True

            elif matrix[row][column] < target: # if value < target
                low = center + 1
            
            else: # if value > target
                high = center - 1

        return False
        
        