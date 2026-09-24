# 36. Valid Sudoku (Medium)
# Time Complexity: O(1) | Space Complexity: O(1)

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue

                # Chỉ số ô 3x3 tương ứng
                box_idx = (r // 3, c // 3)

                # Kiểm tra trùng lặp trong hàng, cột hoặc ô 3x3
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                # Thêm vào tập hợp lưu trữ
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    print(sol.isValidSudoku(board))  # Output: True