# 13. Roman to Integer (Easy)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Duyệt từ phải sang trái
        for char in reversed(s):
            curr_value = roman_map[char]
            
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
                
            prev_value = curr_value
            
        return total

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))      # Output: 3
    print(sol.romanToInt("LVIII"))    # Output: 58
    print(sol.romanToInt("MCMXCIV"))  # Output: 1994