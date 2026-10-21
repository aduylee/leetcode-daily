# 66. Plus One (Easy)
# Time Complexity: O(N) | Space Complexity: O(1) (hoặc O(N) trong trường hợp tất cả là số 9)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Duyệt từ phải sang trái
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        # Nếu tất cả các chữ số đều là 9 (ví dụ: [9, 9] -> [0, 0])
        return [1] + digits

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]

    # Example 2
    print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]

    # Example 3
    print(sol.plusOne([9]))  # Output: [1, 0]