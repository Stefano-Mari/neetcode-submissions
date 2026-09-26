class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        box = {}

        for row_index, row in enumerate(board):
            for col_index, element in enumerate(row):
                if element == ".":
                    continue

                if row_index not in rows:
                    rows[row_index] = set()

                if col_index not in cols:
                    cols[col_index] = set()
                
                if (row_index // 3, col_index // 3) not in box:
                    box[row_index // 3, col_index // 3] = set()

                if element in rows[row_index] or element in cols[col_index] or element in box[row_index // 3, col_index // 3]:
                    return False
                
                rows[row_index].add(element)
                cols[col_index].add(element)
                box[row_index // 3, col_index // 3].add(element)

        return True