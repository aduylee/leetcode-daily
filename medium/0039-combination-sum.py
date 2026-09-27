# 39. Combination Sum (Medium)
# Time Complexity: O(2^T) where T is target | Space Complexity: O(T)

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(start_idx: int, current_target: int, path: list[int]):
            if current_target == 0:
                res.append(path[:])
                return
            if current_target < 0:
                return
            
            for i in range(start_idx, len(candidates)):
                # Chọn candidate[i]
                path.append(candidates[i])
                # Tiếp tục gọi đệ quy với start_idx = i (cho phép chọn lại chính số này)
                backtrack(i, current_target - candidates[i], path)
                # Backtrack
                path.pop()

        backtrack(0, target, [])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]

    # Example 2
    print(sol.combinationSum([2, 3, 5], 8))     # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Example 3
    print(sol.combinationSum([2], 1))           # Output: []