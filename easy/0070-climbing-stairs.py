# 70. Climbing Stairs (Easy)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1  # Số cách leo 1 bậc
        prev1 = 2  # Số cách leo 2 bậc
        current = 0

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.climbStairs(2))  # Output: 2

    # Example 2
    print(sol.climbStairs(3))  # Output: 3
    