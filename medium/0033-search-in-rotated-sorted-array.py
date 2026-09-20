# 33. Search in Rotated Sorted Array (Medium)
# Time Complexity: O(log N) | Space Complexity: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Kiểm tra xem nửa bên trái có sắp xếp hay không
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Nửa bên phải được sắp xếp
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4

    # Example 2
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1

    # Example 3
    print(sol.search([1], 0))                    # Output: -1