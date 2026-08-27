# 10. Regular Expression Matching (Hard)
# Time Complexity: O(M * N) | Space Complexity: O(M * N)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: chuỗi rỗng khớp với pattern rỗng
        dp[0][0] = True
        
        # Xử lý các pattern dạng a*, a*b*, .* với chuỗi rỗng
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Điền bảng DP
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Trường hợp 1: Coi '*' là 0 lần xuất hiện của ký tự trước
                    dp[i][j] = dp[i][j - 2]
                    
                    # Trường hợp 2: Coi '*' là >= 1 lần xuất hiện (nếu ký tự trước khớp với s[i-1])
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    # Ký tự thường hoặc dấu '.'
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                        
        return dp[m][n]