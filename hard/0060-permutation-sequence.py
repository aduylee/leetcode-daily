# 60. Permutation Sequence (Hard)
# Time Complexity: O(N^2) | Space Complexity: O(N)

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Tạo danh sách các số từ 1 đến n
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Chuyển về 0-indexed
        res = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            res.append(numbers.pop(index))
            k %= fact
            
        return "".join(res)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.getPermutation(3, 3))  # Output: "213"

    # Example 2
    print(sol.getPermutation(4, 9))  # Output: "2314"

    # Example 3
    print(sol.getPermutation(3, 1))  # Output: "123"