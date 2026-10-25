# 69. Sqrt(x) (Easy)
# Time Complexity: O(log X) | Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.mySqrt(4))  # Output: 2

    # Example 2
    print(sol.mySqrt(8))  # Output: 2