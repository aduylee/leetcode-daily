# 28. Find the Index of the First Occurrence in a String (Easy)
# Time Complexity: O((N - M) * M) | Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        if m > n:
            return -1
            
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
                
        return -1

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.strStr("sadbutsad", "sad"))  # Output: 0
    
    # Example 2
    print(sol.strStr("leetcode", "leeto"))  # Output: -1