# 17. Letter Combinations of a Phone Number (Medium)
# Time Complexity: O(4^N * N) | Space Complexity: O(N)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index: int, current_path: list[str]):
            # Điều kiện dừng: Đã duyệt hết chuỗi digits
            if index == len(digits):
                res.append("".join(current_path))
                return
            
            # Lấy các ký tự tương ứng với digit hiện tại
            possible_chars = digit_to_char[digits[index]]
            for char in possible_chars:
                current_path.append(char)
                backtrack(index + 1, current_path)
                current_path.pop()  # Quay lui (backtrack)
                
        backtrack(0, [])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(sol.letterCombinations("2"))   # Output: ["a","b","c"]
    print(sol.letterCombinations(""))    # Output: []