# 52. N-Queens II (Hard)
# Time Complexity: O(N!) | Space Complexity: O(N)

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        def backtrack(r: int) -> int:
            if r == n:
                return 1

            count = 0
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                count += backtrack(r + 1)

                # Backtrack
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

            return count

        return backtrack(0)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.totalNQueens(4))  # Output: 2

    # Example 2
    print(sol.totalNQueens(1))  # Output: 1
