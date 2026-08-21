# 3. Longest Substring Without Repeating Characters (Medium)
# Time Complexity: O(N) | Space Complexity: O(min(N, M))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Thu hẹp cửa sổ nếu gặp ký tự đã xuất hiện
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Thêm ký tự mới và cập nhật độ dài tối đa
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.lengthOfLongestSubstring("abcabcbb")) # Output: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))    # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))   # Output: 3