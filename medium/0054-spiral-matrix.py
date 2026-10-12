# 54. Spiral Matrix (Medium)
# Time Complexity: O(M * N) | Space Complexity: O(1) (không tính mảng kết quả)

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Duyệt từ trái sang phải trên hàng `top`
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. Duyệt từ trên xuống dưới trên cột `right`
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. Duyệt từ phải sang trái trên hàng `bottom`
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. Duyệt từ dưới lên trên trên cột `left`
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(m1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Example 2
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(sol.spiralOrder(m2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]