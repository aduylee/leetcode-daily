# 40. Combination Sum II (Medium)
# Time Complexity: O(2^N) | Space Complexity: O(N)

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()  # Sắp xếp để gom số giống nhau và ngắt nhánh sớm
        res = []

        def backtrack(start_idx: int, current_target: int, path: list[int]):
            if current_target == 0:
                res.append(path[:])
                return

            for i in range(start_idx, len(candidates)):
                # Ngắt nhánh sớm nếu số hiện tại lớn hơn target còn lại
                if candidates[i] > current_target:
                    break
                
                # Bỏ qua các phần tử trùng lặp ở cùng một cấp đệ quy
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                # Chuyển sang i + 1 vì mỗi phần tử chỉ dùng 1 lần
                backtrack(i + 1, current_target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    # Example 2
    print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
    # Output: [[1, 2, 2], [5]]