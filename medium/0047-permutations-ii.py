# 47. Permutations II (Medium)
# Time Complexity: O(N * N!) | Space Complexity: O(N)

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Gom các giá trị giống nhau đứng cạnh nhau
        res = []
        used = [False] * len(nums)

        def backtrack(path: list[int]):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Bỏ qua phần tử trùng lặp nếu phần tử đứng trước nó chưa được sử dụng
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                # Backtrack
                path.pop()
                used[i] = False

        backtrack([])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.permuteUnique([1, 1, 2]))  
    # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    # Example 2
    print(sol.permuteUnique([1, 2, 3]))  
    # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]