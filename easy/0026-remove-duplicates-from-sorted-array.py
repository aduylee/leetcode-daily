# 26. Remove Duplicates from Sorted Array (Easy)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
                
        return left

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(f"k = {k1}, nums = {nums1[:k1]}")  # Output: k = 2, nums = [1, 2]
    
    # Example 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(f"k = {k2}, nums = {nums2[:k2]}")  # Output: k = 5, nums = [0, 1, 2, 3, 4]