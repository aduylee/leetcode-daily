# 45. Jump Game II (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        # Duyệt tới n - 2 vì từ n - 1 không cần thực hiện thêm bước nhảy nào
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # Khi chạm tới giới hạn của bước nhảy hiện tại
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.jump([2, 3, 1, 1, 4]))  # Output: 2

    # Example 2
    print(sol.jump([2, 3, 0, 1, 4]))  # Output: 2