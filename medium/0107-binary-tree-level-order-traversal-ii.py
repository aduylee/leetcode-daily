from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 107. Binary Tree Level Order Traversal II (Medium)
# Time Complexity: O(N) - duyệt qua mỗi nút đúng 1 lần
# Space Complexity: O(N) - lưu trữ hàng đợi và danh sách kết quả

class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(current_level)

        return res[::-1]

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1: root = [3, 9, 20, null, null, 15, 7] -> [[15, 7], [9, 20], [3]]
    root1 = TreeNode(3,
                     TreeNode(9),
                     TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.levelOrderBottom(root1))  # Output: [[15, 7], [9, 20], [3]][cite: 14]

    # Test Example 2: root = [1] -> [[1]]
    print(sol.levelOrderBottom(TreeNode(1)))  # Output: [[1]][cite: 14]

    # Test Example 3: root = [] -> []
    print(sol.levelOrderBottom(None))  # Output: [][cite: 14]