# 59. Spiral Matrix II (Medium)
# Time Complexity: O(N^2) | Space Complexity: O(1) (không tính không gian ma trận trả về)

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        target = n * n

        while num <= target:
            # 1. Điền từ trái sang phải trên hàng `top`
            for c in range(left, right + 1):
                matrix[top][c] = num
                num += 1
            top += 1

            # 2. Điền từ trên xuống dưới trên cột `right`
            for r in range(top, bottom + 1):
                matrix[r][right] = num
                num += 1
            right -= 1

            # 3. Điền từ phải sang trái trên hàng `bottom`
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = num
                num += 1
            bottom -= 1

            # 4. Điền từ dưới lên trên trên cột `left`
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = num
                num += 1
            left += 1

        return matrix

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.generateMatrix(3))
    # Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    # Example 2
    print(sol.generateMatrix(1))
    # Output: [[1]]