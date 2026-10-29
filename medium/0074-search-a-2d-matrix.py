# 74. Search a 2D Matrix (Medium)
# Time Complexity: O(log(m * n)) | Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // n
            c = mid % n
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(sol.searchMatrix(matrix1, 3))   # Output: True

    # Example 2
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(sol.searchMatrix(matrix2, 13))  # Output: False