# 80. Remove Duplicates from Sorted Array II (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for num in nums:
            if k < 2 or num > nums[k - 2]:
                nums[k] = num
                k += 1
        return k

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = sol.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # Output: 5, [1, 1, 2, 2, 3]

    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = sol.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # Output: 7, [0, 0, 1, 1, 2, 3, 3]