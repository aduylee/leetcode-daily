# 50. Pow(x, n) (Medium)
# Time Complexity: O(log N) | Space Complexity: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        N = n
        if N < 0:
            x = 1 / x
            N = -N

        res = 1.0
        current_product = x

        while N > 0:
            # Nếu N là số lẻ
            if N % 2 == 1:
                res *= current_product
            
            current_product *= current_product
            N //= 2

        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(f"{sol.myPow(2.00000, 10):.5f}")  # Output: 1024.00000

    # Example 2
    print(f"{sol.myPow(2.10000, 3):.5f}")   # Output: 9.26100

    # Example 3
    print(f"{sol.myPow(2.00000, -2):.5f}")  # Output: 0.25000