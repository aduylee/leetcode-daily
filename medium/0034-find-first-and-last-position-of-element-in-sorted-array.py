# 34. Find First and Last Position of Element in Sorted Array (Medium)
# Time Complexity: O(log N) | Space Complexity: O(1)

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1  # Tìm tiếp bên trái cho vị trí đầu tiên
                    else:
                        left = mid + 1   # Tìm tiếp bên phải cho vị trí cuối cùng
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        return [find_bound(True), find_bound(False)]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]

    # Example 2
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: [-1, -1]

    # Example 3
    print(sol.searchRange([], 0))                   # Output: [-1, -1]