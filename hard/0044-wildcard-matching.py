# 44. Wildcard Matching (Hard)
# Time Complexity: O(M * N) worst case, O(M + N) average | Space Complexity: O(1)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = p_ptr = 0
        star_idx = -1
        s_tmp_idx = -1

        while s_ptr < len(s):
            # Ký tự khớp nhau hoặc gặp '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            # Gặp dấu '*' trong pattern
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp_idx = s_ptr
                p_ptr += 1
            # Không khớp nhưng có dấu '*' trước đó -> Backtrack cho '*' ăn thêm 1 ký tự
            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_tmp_idx += 1
                s_ptr = s_tmp_idx
            else:
                return False

        # Kiểm tra nếu còn các dấu '*' thừa ở cuối pattern
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1

        return p_ptr == len(p)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.isMatch("aa", "a"))   # Output: False

    # Example 2
    print(sol.isMatch("aa", "*"))   # Output: True

    # Example 3
    print(sol.isMatch("cb", "?a"))  # Output: False