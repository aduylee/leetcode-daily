# 88. Merge Sorted Array (Easy)
# Time Complexity: O(m + n) | Space Complexity: O(1)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Gộp từ cuối về đầu
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Nếu nums2 vẫn còn phần tử, copy vào nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

    nums2 = [1]
    sol.merge(nums2, 1, [], 0)
    print(nums2)  # Output: [1]