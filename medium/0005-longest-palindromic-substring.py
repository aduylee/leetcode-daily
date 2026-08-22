# 5. Longest Palindromic Substring (Medium)
# Time Complexity: O(N^2) | Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            # Mở rộng sang 2 bên khi 2 ký tự ở biên bằng nhau
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Độ dài chuỗi đối xứng vừa tìm được
            return right - left - 1
        
        for i in range(len(s)):
            # Trường hợp 1: Tâm là 1 ký tự (chuỗi lẻ)
            len1 = expand_around_center(i, i)
            # Trường hợp 2: Tâm là 2 ký tự (chuỗi chẵn)
            len2 = expand_around_center(i, i + 1)
            
            # Lấy độ dài lớn hơn
            max_len = max(len1, len2)
            
            # Cập nhật vị trí bắt đầu và kết thúc của chuỗi dài nhất
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # Output: "bab" hoặc "aba"
    print(sol.longestPalindrome("cbbd"))   # Output: "bb"