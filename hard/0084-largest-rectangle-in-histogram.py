# 84. Largest Rectangle in Histogram (Hard)
# Time Complexity: O(N) | Space Complexity: O(N)

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # Thêm chiều cao giả lập 0 ở cuối để clear toàn bộ stack
            current_height = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > current_height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Output: 10[cite: 7]
    print(sol.largestRectangleArea([2, 4]))                # Output: 4