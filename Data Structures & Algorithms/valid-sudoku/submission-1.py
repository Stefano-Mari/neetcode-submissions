class Solution:
    # Time: O(n^2), Space: O(n^2), where n = number of rows
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        box = {}

        for row_index, row in enumerate(board): # O(n)
            for col_index, element in enumerate(row): # O(n)
                if element == ".": 
                    continue

                if row_index not in rows: # O(1) - hashmap key lookup
                    rows[row_index] = set()

                if col_index not in cols: # O(1) - hashmap key lookup
                    cols[col_index] = set()
                
                if (row_index // 3, col_index // 3) not in box: # O(1) - hashmap key lookup
                    box[row_index // 3, col_index // 3] = set()

                # O(1) - hashset key lookup
                if element in rows[row_index] or element in cols[col_index] or element in box[row_index // 3, col_index // 3]: 
                    return False
                
                rows[row_index].add(element)
                cols[col_index].add(element)
                box[row_index // 3, col_index // 3].add(element)

        return True