# 65. Valid Number (Hard)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in "+-":
                # Dấu chỉ hợp lệ ở đầu chuỗi hoặc ngay sau 'e'/'E'
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char == '.':
                # Dấu chấm không được xuất hiện nếu đã có dấu chấm hoặc đã có 'e'/'E'
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                # 'e'/'E' chỉ hợp lệ nếu chưa xuất hiện trước đó và đã có ít nhất một số đứng trước
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Bắt buộc phải có chữ số sau 'e'/'E'
            else:
                return False
                
        return seen_digit

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Hợp lệ
    print(sol.isNumber("2"))          # True
    print(sol.isNumber("0089"))       # True
    print(sol.isNumber("-0.1"))       # True
    print(sol.isNumber("+3.14"))      # True
    print(sol.isNumber("4."))         # True
    print(sol.isNumber("-.9"))        # True
    print(sol.isNumber("2e10"))       # True

    # Không hợp lệ
    print(sol.isNumber("abc"))        # False
    print(sol.isNumber("1a"))         # False
    print(sol.isNumber("1e"))         # False
    print(sol.isNumber("99e2.5"))     # False