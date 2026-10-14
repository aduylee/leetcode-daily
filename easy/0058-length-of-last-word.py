# 58. Length of Last Word (Easy)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # Bỏ qua các dấu cách ở cuối chuỗi
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Đếm độ dài của từ cuối cùng
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.lengthOfLastWord("Hello World"))         # Output: 5

    # Example 2
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4

    # Example 3
    print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6