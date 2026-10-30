# 67. Add Binary (Easy)
# Time Complexity: O(max(N, M)) | Space Complexity: O(max(N, M))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            
            res.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(res))

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.addBinary("11", "1"))     # Output: "100"

    # Example 2
    print(sol.addBinary("1010", "1011")) # Output: "10101"