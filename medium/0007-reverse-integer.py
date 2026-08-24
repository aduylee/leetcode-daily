# 7. Reverse Integer (Medium)
# Time Complexity: O(log10(N)) | Space Complexity: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        # Xác định dấu (+1 hoặc -1)
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Đảo ngược các chữ số
        reversed_x = int(str(x)[::-1]) * sign
        
        # Kiểm tra giới hạn 32-bit
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
            
        return reversed_x

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))   # Output: 321
    print(sol.reverse(-123))  # Output: -321
    print(sol.reverse(120))   # Output: 21
    