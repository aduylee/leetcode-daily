# 78. Subsets (Medium)
# Time Complexity: O(2^n * n) | Space Complexity: O(2^n * n)

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(start: int, path: list[int]):
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))  # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(sol.subsets([0]))        # Output: [[],[0]]