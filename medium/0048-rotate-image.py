# 48. Rotate Image (Medium)
# Time Complexity: O(N^2) | Space Complexity: O(1)

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Bước 1: Chuyển vị ma trận (Transpose)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Bước 2: Đảo ngược từng hàng (Reverse)
        for i in range(n):
            matrix[i].reverse()

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(m1)
    print(m1)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Example 2
    m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(m2)
    print(m2)  # Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]