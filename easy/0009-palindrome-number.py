# 9. Palindrome Number (Easy)
# Time Complexity: O(N) | Space Complexity: O(N)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Số âm không bao giờ là Palindrome
        if x < 0:
            return False
            
        # So sánh chuỗi ban đầu và chuỗi đảo ngược
        s = str(x)
        return s == s[::-1]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # Output: True
    print(sol.isPalindrome(-121))  # Output: False
    print(sol.isPalindrome(10))    # Output: False