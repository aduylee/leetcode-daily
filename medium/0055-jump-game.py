# 55. Jump Game (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
                
        return True

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.canJump([2, 3, 1, 1, 4]))  # Output: True

    # Example 2
    print(sol.canJump([3, 2, 1, 0, 4]))  # Output: False