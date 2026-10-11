# 53. Maximum Subarray (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6

    # Example 2
    print(sol.maxSubArray([1]))                              # Output: 1

    # Example 3
    print(sol.maxSubArray([5, 4, -1, 7, 8]))                  # Output: 23
