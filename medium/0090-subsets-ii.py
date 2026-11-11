# 90. Subsets II (Medium)
# Time Complexity: O(N * 2^N) | Space Complexity: O(N * 2^N)

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        def backtrack(start: int, path: list[int]):
            res.append(path.copy())
            
            for i in range(start, len(nums)):
                # Bỏ qua các phần tử trùng lặp ở cùng một tầng đệ quy
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1, 2, 2]))  # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(sol.subsetsWithDup([0]))        # Output: [[],[0]]