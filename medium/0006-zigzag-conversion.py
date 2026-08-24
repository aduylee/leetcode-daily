# 6. Zigzag Conversion (Medium)
# Time Complexity: O(N) | Space Complexity: O(N)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Nếu chỉ có 1 hàng hoặc chiều dài s nhỏ hơn numRows thì trả về nguyên gốc s
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Mảng chứa chuỗi cho từng hàng
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            # Đổi hướng khi chạm biên trên (hàng 0) hoặc biên dưới (hàng numRows - 1)
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Di chuyển lên hoặc xuống
            current_row += 1 if going_down else -1
            
        # Nối tất cả các hàng lại thành chuỗi kết quả
        return "".join(rows)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedian("PAYPALISHIRING", 3) if hasattr(sol, 'findMedian') else sol.convert("PAYPALISHIRING", 3)) # Output: "PAHNAPLSIIGYIR"
    print(sol.convert("PAYPALISHIRING", 4)) # Output: "PINALSIGYAHRPI"