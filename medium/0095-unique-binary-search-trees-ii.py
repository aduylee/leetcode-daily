# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 95. Unique Binary Search Trees II (Medium)
# Time Complexity: O(4^n / sqrt(n)) - Số Catalan thứ n
# Space Complexity: O(4^n / sqrt(n))

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []
            
        memo = {}

        def build_trees(start: int, end: int) -> list[TreeNode | None]:
            if start > end:
                return [None]
                
            if (start, end) in memo:
                return memo[(start, end)]
                
            all_trees = []
            # Chọn từng giá trị i trong [start, end] làm nút gốc
            for i in range(start, end + 1):
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)
                
                # Kết hợp mọi cặp cây con trái và cây con phải
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
                        
            memo[(start, end)] = all_trees
            return all_trees

        return build_trees(1, n)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    trees_3 = sol.generateTrees(3)
    print(f"Số lượng BST với n = 3: {len(trees_3)}")  # Output: 5[cite: 9]
    
    trees_1 = sol.generateTrees(1)
    print(f"Số lượng BST với n = 1: {len(trees_1)}")  # Output: 1[cite: 9]