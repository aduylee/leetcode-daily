# 31. Next Permutation (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not modify anything in-place, return nums instead.
        """
        n = len(nums)
        i = n - 2

        # 1. Tìm chỉ số i đầu tiên từ phải sang sao cho nums[i] < nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 2. Tìm chỉ số j từ phải sang sao cho nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Hoán đổi nums[i] và nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Đảo ngược đoạn mảng từ i + 1 đến hết
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [1, 2, 3]
    sol.nextPermutation(nums1)
    print(nums1)  # Output: [1, 3, 2]

    # Example 2
    nums2 = [3, 2, 1]
    sol.nextPermutation(nums2)
    print(nums2)  # Output: [1, 2, 3]

    # Example 3
    nums3 = [1, 1, 5]
    sol.nextPermutation(nums3)
    print(nums3)  # Output: [1, 5, 1]