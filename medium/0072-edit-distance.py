# 72. Edit Distance (Hard)
# Time Complexity: O(m * n) | Space Complexity: O(n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Đảm bảo word2 ngắn hơn để tối ưu không gian O(min(m, n))
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m
            
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            new_dp = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    new_dp[j] = dp[j - 1]
                else:
                    new_dp[j] = 1 + min(dp[j],      # Delete
                                        new_dp[j - 1], # Insert
                                        dp[j - 1])    # Replace
            dp = new_dp
            
        return dp[n]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))           # Output: 3
    print(sol.minDistance("intention", "execution")) # Output: 5