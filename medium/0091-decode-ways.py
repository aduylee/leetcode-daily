# 91. Decode Ways (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i+1], dp[i+2] tương ứng với các trạng thái phía sau
        next_to_next = 1  # Tương đương dp[n]
        next_val = 1      # Tương đương dp[n-1]
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                current = 0
            else:
                current = next_val
                # Kiểm tra nếu ghép với ký tự tiếp theo tạo thành số từ 10 đến 26
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    current += next_to_next
            
            next_to_next = next_val
            next_val = current
            
        return next_val

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))      # Output: 2 ("1","2" hoặc "12")
    print(sol.numDecodings("226"))     # Output: 3 ("2","2","6" hoặc "22","6" hoặc "2","26")
    print(sol.numDecodings("06"))      # Output: 0 (không hợp lệ vì bắt đầu bằng '0')