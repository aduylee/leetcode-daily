# 64. Minimum Path Sum (Medium)
# Time Complexity: O(m * n) | Space Complexity: O(n)

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0

        for r in range(m):
            dp[0] += grid[r][0]
            for c in range(1, n):
                dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

        return dp[-1]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(grid1))  # Output: 7

    # Example 2
    grid2 = [[1, 2, 3], [4, 5, 6]]
    print(sol.minPathSum(grid2))  # Output: 12