# 43. Multiply Strings (Medium)
# Time Complexity: O(M * N) | Space Complexity: O(M + N)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # Duyệt ngược từng chữ số của num1 và num2
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10

        # Chuyển đổi mảng res thành chuỗi, bỏ các số 0 vô nghĩa ở đầu
        result_str = "".join(map(str, res))
        return result_str.lstrip("0")

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.multiply("2", "3"))        # Output: "6"

    # Example 2
    print(sol.multiply("123", "456"))    # Output: "56088"