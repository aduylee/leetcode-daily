# 46. Permutations (Medium)
# Time Complexity: O(N * N!) | Space Complexity: O(N)

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        visited = set()

        def backtrack(path: list[int]):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    
                    backtrack(path)
                    
                    # Backtrack
                    path.pop()
                    visited.remove(num)

        backtrack([])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.permute([1, 2, 3]))  
    # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    # Example 2
    print(sol.permute([0, 1]))     
    # Output: [[0, 1], [1, 0]]

    # Example 3
    print(sol.permute([1]))        
    # Output: [[1]]