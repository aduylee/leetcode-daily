# 20. Valid Parentheses (Easy)
# Time Complexity: O(N) | Space Complexity: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Lấy phần tử đỉnh stack nếu stack không rỗng, ngược lại lấy ký tự giả '#'
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # Ký tự là ngoặc mở
                stack.append(char)
                
        # Trả về True nếu tất cả ngoặc mở đã được đóng hết
        return not stack

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))      # Output: True
    print(sol.isValid("()[]{}"))  # Output: True
    print(sol.isValid("(]"))      # Output: False
    print(sol.isValid("([])"))    # Output: True