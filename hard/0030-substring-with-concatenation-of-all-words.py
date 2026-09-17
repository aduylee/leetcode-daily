# 30. Substring with Concatenation of All Words (Hard)
# Time Complexity: O(N * L_w) | Space Complexity: O(M * L_w)
# (với N là độ dài chuỗi s, M là số lượng từ trong words, L_w là độ dài mỗi từ)

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []
            
        word_count = Counter(words)
        res = []
        
        # Duyệt qua từng offset có thể có (từ 0 đến word_len - 1)
        for i in range(word_len):
            left = i
            seen = Counter()
            count = 0
            
            # Nhảy từng bước có độ dài word_len
            for right in range(i, s_len - word_len + 1, word_len):
                sub = s[right : right + word_len]
                
                if sub in word_count:
                    seen[sub] += 1
                    count += 1
                    
                    # Nếu tần suất xuất hiện vượt quá quy định, thu hẹp cửa sổ từ bên trái
                    while seen[sub] > word_count[sub]:
                        left_sub = s[left : left + word_len]
                        seen[left_sub] -= 1
                        count -= 1
                        left += word_len
                        
                    # Nếu thu thập đủ số lượng từ
                    if count == num_words:
                        res.append(left)
                else:
                    # Nếu từ không nằm trong words, reset lại cửa sổ
                    seen.clear()
                    count = 0
                    left = right + word_len
                    
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    # Output: [0, 9]
    
    # Example 2
    print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    # Output: []
    
    # Example 3
    print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    # Output: [6, 9, 12]