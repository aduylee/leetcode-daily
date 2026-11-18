# 97. Interleaving String (Medium)
# Time Complexity: O(M * N) | Space Complexity: O(N)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        # Tối ưu không gian: đảm bảo s2 là chuỗi ngắn hơn để mảng dp nhỏ nhất
        if n > m:
            s1, s2 = s2, s1
            m, n = n, m
            
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Khởi tạo hàng đầu tiên (chỉ dùng các ký tự của s2)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        # Cập nhật từng hàng tiếp theo
        for i in range(1, m + 1):
            # Cột đầu tiên (chỉ dùng các ký tự của s1)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = from_s1 or from_s2
                
        return dp[n]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # Output: True
    print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # Output: False
    print(sol.isInterleave("", "", ""))                        # Output: True