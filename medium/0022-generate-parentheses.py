# 22. Generate Parentheses (Medium)
# Time Complexity: O(4^n / sqrt(n)) | Space Complexity: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count: int, close_count: int, current_str: str):
            # Điều kiện dừng: Chuỗi đủ độ dài 2 * n
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Thêm ngoặc mở nếu chưa vượt quá n
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Thêm ngoặc đóng nếu số ngoặc đóng ít hơn ngoặc mở
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")
                
        backtrack(0, 0, "")
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
    print(sol.generateParenthesis(1))  # Output: ["()"]git pull --rebase origin main
