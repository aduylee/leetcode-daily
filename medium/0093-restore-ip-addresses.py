# 93. Restore IP Addresses (Medium)
# Time Complexity: O(1) - Số lượng IP tối đa có thể tạo ra là giới hạn (hữu hạn)
# Space Complexity: O(1) - Không gian đệ quy tối đa 4 tầng

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        n = len(s)
        
        # Cắt chuỗi thành 4 phần sử dụng chỉ số bắt đầu của từng phần
        def backtrack(startIndex: int, path: list[str]):
            # Nếu đã đủ 4 phần
            if len(path) == 4:
                # Nếu đã dùng hết toàn bộ chuỗi s, ta thu được 1 IP hợp lệ
                if startIndex == n:
                    res.append(".".join(path))
                return
            
            # Thử cắt từ 1 đến 3 ký tự cho phần hiện tại
            for length in range(1, 4):
                if startIndex + length > n:
                    break
                
                segment = s[startIndex:startIndex + length]
                
                # Kiểm tra tính hợp lệ của segment:
                # 1. Không có số 0 ở đầu nếu độ dài > 1 (ví dụ: "01" không hợp lệ, nhưng "0" hợp lệ)
                # 2. Giá trị số nguyên không được vượt quá 255
                if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                
                path.append(segment)
                backtrack(startIndex + length, path)
                path.pop()
                
        backtrack(0, [])
        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))  # Output: ["255.255.11.135","255.255.111.35"]
    print(sol.restoreIpAddresses("0000"))         # Output: ["0.0.0.0"]
    print(sol.restoreIpAddresses("101023"))       # Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]