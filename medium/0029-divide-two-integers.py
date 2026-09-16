# 29. Divide Two Integers (Medium)
# Time Complexity: O(log^2 N) | Space Complexity: O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Giới hạn số nguyên 32-bit
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Xử lý trường hợp tràn số (Overflow)
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Xác định dấu của kết quả
        negative = (dividend < 0) ^ (divisor < 0)

        # Chuyển về giá trị tuyệt đối
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # Phép chia dùng bit shift
        while a >= b:
            temp_b, count = b, 1
            while a >= (temp_b << 1):
                temp_b <<= 1
                count <<= 1
            
            a -= temp_b
            quotient += count

        # Trả về kết quả theo đúng dấu
        return -quotient if negative else quotient

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.divide(10, 3))   # Output: 3
    
    # Example 2
    print(sol.divide(7, -3))   # Output: -2