# 37. Sudoku Solver (Hard)
# Time Complexity: O(9^(N)) where N is number of empty cells | Space Complexity: O(1)

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not modify anything in-place, return board instead.
        """
        def is_valid(r: int, c: int, val: str) -> bool:
            for i in range(9):
                # Kiểm tra hàng
                if board[r][i] == val:
                    return False
                # Kiểm tra cột
                if board[i][c] == val:
                    return False
                # Kiểm tra khối 3x3
                box_r = 3 * (r // 3) + i // 3
                box_c = 3 * (c // 3) + i % 3
                if board[box_r][box_c] == val:
                    return False
            return True

        def backtrack() -> bool:
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(r, c, num):
                                board[r][c] = num
                                if backtrack():
                                    return True
                                board[r][c] = "."  # Backtrack
                        return False  # Không có số nào hợp lệ
            return True  # Đã điền xong tất cả ô trống

        backtrack()

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

    sol.solveSudoku(board)
    for row in board:
        print(row)