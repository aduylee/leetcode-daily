# 8. String to Integer (atoi) (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Bỏ khoảng trắng ở đầu
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        # Kiểm tra dấu
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
            
        res = 0
        # Đọc các chữ số liên tiếp
        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])
            index += 1
            
        res *= sign
        
        # Xử lý tràn số 32-bit (Clamping)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))             # Output: 42
    print(sol.myAtoi("   -042"))        # Output: -42
    print(sol.myAtoi("1337c0d3"))       # Output: 1337
    print(sol.myAtoi("0-1"))            # Output: 0
    print(sol.myAtoi("words and 987"))  # Output: 0