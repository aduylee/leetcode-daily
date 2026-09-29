# 41. First Missing Positive (Hard)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Bước 1: Đưa các số trong khoảng [1, n] về đúng vị trí của chúng (nums[i] -> index nums[i] - 1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Hoán đổi nums[i] về đúng chỉ số nums[i] - 1
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Bước 2: Tìm vị trí đầu tiên không chứa đúng số tương ứng
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.firstMissingPositive([1, 2, 0]))          # Output: 3

    # Example 2
    print(sol.firstMissingPositive([3, 4, -1, 1]))       # Output: 2

    # Example 3
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))   # Output: 1