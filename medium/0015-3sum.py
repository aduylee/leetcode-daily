# 15. 3Sum (Medium)
# Time Complexity: O(N^2) | Space Complexity: O(1) or O(N) depending on sorting implementation

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            # Optimization: Nếu số nhỏ nhất > 0 thì tổng 3 số không thể bằng 0
            if nums[i] > 0:
                break
                
            # Bỏ qua các phần tử trùng lặp cho vị trí thứ nhất
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Bỏ qua trùng lặp cho con trỏ left và right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 1, 1]))               # Output: []
    print(sol.threeSum([0, 0, 0]))               # Output: [[0, 0, 0]]