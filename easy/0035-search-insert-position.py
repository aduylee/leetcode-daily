# 35. Search Insert Position (Easy)
# Time Complexity: O(log N) | Space Complexity: O(1)

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.searchInsert([1, 3, 5, 6], 5))  # Output: 2

    # Example 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # Output: 1

    # Example 3
    print(sol.searchInsert([1, 3, 5, 6], 7))  # Output: 4