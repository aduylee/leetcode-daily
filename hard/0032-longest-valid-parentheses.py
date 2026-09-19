# 32. Longest Valid Parentheses (Hard)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        
        # Lần 1: Duyệt từ trái sang phải
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
                
        left = right = 0
        
        # Lần 2: Duyệt từ phải sang trái
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
                
        return max_len

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.longestValidParentheses("(()"))      # Output: 2
    
    # Example 2
    print(sol.longestValidParentheses(")()())"))   # Output: 4
    
    # Example 3
    print(sol.longestValidParentheses(""))         # Output: 0