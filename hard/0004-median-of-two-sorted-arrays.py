# 4. Median of Two Sorted Arrays (Hard)
# Time Complexity: O(log(min(M, N))) | Space Complexity: O(1)

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Đảm bảo nums1 luôn là mảng nhỏ hơn để tối ưu phạm vi Binary Search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Số phần tử cần có ở nửa bên trái
        
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2  # Số phần tử lấy từ nums1
            j = half - i             # Số phần tử lấy từ nums2
            
            # Lấy các giá trị biên (dùng -inf và inf để xử lý trường hợp chạm viền mảng)
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # Kiểm tra vạch cắt hợp lệ
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Nếu tổng số phần tử là LẺ
                if total % 2 != 0:
                    return float(max(nums1_left, nums2_left))
                # Nếu tổng số phần tử là CHẴN
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                right = i - 1  # Cắt quá nhiều phần tử ở nums1 -> giảm right
            else:
                left = i + 1   # Cắt quá ít phần tử ở nums1 -> tăng left

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))    # Output: 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4])) # Output: 2.5