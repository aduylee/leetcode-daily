# 63. Unique Paths II (Medium)
# Time Complexity: O(m * n) | Space Complexity: O(n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c - 1]

        return dp[-1]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    grid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(sol.uniquePathsWithObstacles(grid1))  # Output: 2

    # Example 2
    grid2 = [[0, 1], [0, 0]]
    print(sol.uniquePathsWithObstacles(grid2))  # Output: 1