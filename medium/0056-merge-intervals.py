# 56. Merge Intervals (Medium)
# Time Complexity: O(N log N) | Space Complexity: O(N)

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # Sắp xếp các khoảng theo điểm bắt đầu tăng dần
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged[-1]

            # Kiểm tra xem có chồng lấp không
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)

        return merged

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]

    # Example 2
    print(sol.merge([[1, 4], [4, 5]]))                     # Output: [[1, 5]]

    # Example 3
    print(sol.merge([[4, 7], [1, 4]]))                     # Output: [[1, 7]]