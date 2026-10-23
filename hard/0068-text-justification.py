# 68. Text Justification (Hard)
# Time Complexity: O(N) | Space Complexity: O(maxWidth)

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        current_line = []
        current_length = 0

        for word in words:
            # Kiểm tra xem thêm từ mới có vượt quá maxWidth không
            # current_length + len(current_line) là số ký tự cộng với các khoảng trắng tối thiểu giữa các từ
            if current_length + len(current_line) + len(word) > maxWidth:
                # Xử lý căn lề cho dòng hiện tại
                if len(current_line) == 1:
                    line = current_line[0] + " " * (maxWidth - current_length)
                else:
                    total_spaces = maxWidth - current_length
                    num_slots = len(current_line) - 1
                    spaces_per_slot = total_spaces // num_slots
                    extra_spaces = total_spaces % num_slots
                    
                    line = ""
                    for i in range(num_slots):
                        space_to_add = spaces_per_slot + (1 if i < extra_spaces else 0)
                        line += current_line[i] + " " * space_to_add
                    line += current_line[-1]  # Thêm từ cuối cùng của dòng
                
                res.append(line)
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)

        # Xử lý dòng cuối cùng (left-justified)
        last_line = " ".join(current_line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)

        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    print(sol.fullJustify(words1, maxWidth1))
    # Output: ["This    is    an", "example  of text", "justification.  "]