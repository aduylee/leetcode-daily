# 16. 3Sum Closest (Medium)
# Time Complexity: O(N^2) | Space Complexity: O(1)

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Nếu tìm thấy tổng bằng đúng target, trả về luôn
                if current_sum == target:
                    return current_sum
                
                # Cập nhật kết quả gần target nhất
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Di chuyển con trỏ
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
    print(sol.threeSumClosest([0, 0, 0], 1))        # Output: 0