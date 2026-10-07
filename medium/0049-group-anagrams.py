# 49. Group Anagrams (Medium)
# Time Complexity: O(N * K log K) | Space Complexity: O(N * K)
# (N là số lượng chuỗi, K là độ dài tối đa của một chuỗi)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Dùng chuỗi sau khi sắp xếp làm key
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)

        return list(anagram_map.values())

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    # Example 2
    print(sol.groupAnagrams([""]))
    # Output: [[""]]

    # Example 3
    print(sol.groupAnagrams(["a"]))
    # Output: [["a"]]