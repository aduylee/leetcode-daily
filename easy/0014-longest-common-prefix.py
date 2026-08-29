# 14. Longest Common Prefix (Easy)
# Time Complexity: O(N * M * log N) | Space Complexity: O(M) 
# (với N là số lượng chuỗi, M là độ dài trung bình của chuỗi)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        # Sắp xếp mảng chuỗi theo thứ tự từ điển
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        i = 0
        
        # So sánh từng ký tự của chuỗi đầu và chuỗi cuối
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""