# 12. Integer to Roman (Medium)
# Time Complexity: O(1) | Space Complexity: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        # Danh sách các cặp (giá trị, ký hiệu La Mã) từ lớn đến nhỏ
        val_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        for val, symbol in val_to_roman:
            if num == 0:
                break
            count = num // val
            result.append(symbol * count)
            num %= val
            
        return "".join(result)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3749))  # Output: "MMMDCCXLIX"
    print(sol.intToRoman(58))    # Output: "LVIII"
    print(sol.intToRoman(1994))  # Output: "MCMXCIV"