# 1. Two Sum (Easy)
# Time Complexity: O(n) | Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
    # Khởi tạo class và chạy thử
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Kết quả mong đợi: [0, 1]
print(sol.twoSum([3, 2, 4], 6))       # Kết quả mong đợi: [1, 2]