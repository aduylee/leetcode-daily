# 79. Word Search (Medium)
# Time Complexity: O(M * N * 3^L) | Space Complexity: O(L) với L là độ dài của word

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)

        def dfs(r: c, c: int, idx: int) -> bool:
            # Nếu đã khớp hết tất cả các ký tự của word
            if idx == L:
                return True
            
            # Kiểm tra biên và điều kiện khớp ký tự
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False

            # Đánh dấu ô hiện tại đã được thăm
            temp = board[r][c]
            board[r][c] = '#'

            # Duyệt 4 hướng: xuống, lên, phải, trái
            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # Phục hồi lại giá trị cũ của ô
            board[r][c] = temp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    print(sol.exist(board, "ABCCED"))  # Output: True[cite: 3]
    print(sol.exist(board, "SEE"))     # Output: True[cite: 3]
    print(sol.exist(board, "ABCB"))    # Output: False