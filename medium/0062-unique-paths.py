# 62. Unique Paths (Medium)
# Time Complexity: O(m * n) | Space Complexity: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]

        return dp[-1]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.uniquePaths(3, 7))  # Output: 28

    # Example 2
    print(sol.uniquePaths(3, 2))  # Output: 3