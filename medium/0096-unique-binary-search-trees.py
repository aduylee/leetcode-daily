# 96. Unique Binary Search Trees (Medium)
# Time Complexity: O(N^2) | Space Complexity: O(N)

class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] lưu số lượng BST độc nhất với i nút
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # Tính lần lượt từ 2 nút đến n nút
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_trees = dp[root - 1]
                right_trees = dp[nodes - root]
                dp[nodes] += left_trees * right_trees

        return dp[n]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees(3))  # Output: 5
    print(sol.numTrees(1))  # Output: 1