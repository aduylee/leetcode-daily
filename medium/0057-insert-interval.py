# 57. Insert Interval (Medium)
# Time Complexity: O(N) | Space Complexity: O(N)

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1. Thêm các khoảng nằm hoàn toàn bên trái `newInterval`
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. Gộp tất cả các khoảng chồng lấp với `newInterval`
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3. Thêm các khoảng nằm hoàn toàn bên phải `newInterval`
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.insert([[1, 3], [6, 9]], [2, 5]))  # Output: [[1, 5], [6, 9]]

    # Example 2
    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # Output: [[1, 2], [3, 10], [12, 16]]