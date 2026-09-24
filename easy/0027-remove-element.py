# 27. Remove Element (Easy)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print(f"k = {k1}, nums = {nums1[:k1]}")  # Output: k = 2, nums = [2, 2]
    
    # Example 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = sol.removeElement(nums2, val2)
    print(f"k = {k2}, nums = {nums2[:k2]}")  # Output: k = 5, nums = [0, 1, 3, 0, 4] (thứ tự tùy thuộc)