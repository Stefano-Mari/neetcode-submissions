class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        combined = []

        for row in matrix:
            combined.extend(row)

        print(combined)

        low = 0
        high = len(combined) - 1

        while low <= high:
            center = (high + low) // 2

            if combined[center] == target:
                return True

            elif combined[center] < target:
                low = center + 1
            
            else:
                high = center - 1

        return False
        
        