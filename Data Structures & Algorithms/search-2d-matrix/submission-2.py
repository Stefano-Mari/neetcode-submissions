class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = (len(matrix) * (len(matrix[0])) - 1)
        
        while low <= high:
            center = (low + high) // 2
            row, column = divmod(center, len(matrix[0]))

            if matrix[row][column] == target:
                return True

            elif matrix[row][column] < target:
                low = center + 1
            
            else:
                high = center - 1

        return False
        
        