# 73. Set Matrix Zeroes (Medium)
# Time Complexity: O(m * n) | Space Complexity: O(1)

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        col0 = 1

        # Bước 1: Đánh dấu các hàng và cột cần chuyển về 0
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Bước 2: Cập nhật các ô bên trong dựa vào đánh dấu
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Bước 3: Cập nhật hàng đầu tiên
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Bước 4: Cập nhật cột đầu tiên
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix1)
    print(matrix1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix2)
    print(matrix2)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]