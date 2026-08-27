# 11. Container With Most Water (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Tính diện tích nước hiện tại
            current_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_water)
            
            # Di chuyển con trỏ của cột ngắn hơn
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
    print(sol.maxArea([1, 1]))                        # Output: 1