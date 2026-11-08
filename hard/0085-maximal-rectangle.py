# 85. Maximal Rectangle (Hard)
# Time Complexity: O(rows * cols) | Space Complexity: O(cols)

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(ht: list[int]) -> int:
            stack = []
            res = 0
            n = len(ht)
            for i in range(n + 1):
                h = ht[i] if i < n else 0
                while stack and ht[stack[-1]] > h:
                    height = ht[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(i)
            return res

        for row in matrix:
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(sol.maximalRectangle(matrix1))  # Output: 6[cite: 7]

    matrix2 = [["0"]]
    print(sol.maximalRectangle(matrix2))  # Output: 0[cite: 7]