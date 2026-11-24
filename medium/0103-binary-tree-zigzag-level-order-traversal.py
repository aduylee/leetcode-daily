from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 103. Binary Tree Zigzag Level Order Traversal (Medium)
# Time Complexity: O(N) - duyệt qua mỗi nút đúng 1 lần
# Space Complexity: O(N) - lưu trữ hàng đợi và danh sách kết quả

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        left_to_right = True

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

            # Đảo ngược danh sách nếu tầng hiện tại duyệt từ phải sang trái
            if not left_to_right:
                current_level.reverse()

            res.append(current_level)
            left_to_right = not left_to_right

        return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1: root = [3, 9, 20, null, null, 15, 7] -> [[3], [20, 9], [15, 7]]
    root1 = TreeNode(3,
                     TreeNode(9),
                     TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.zigzagLevelOrder(root1))  # Output: [[3], [20, 9], [15, 7]]

    # Test Example 2: root = [1] -> [[1]]
    print(sol.zigzagLevelOrder(TreeNode(1)))  # Output: [[1]]

    # Test Example 3: root = [] -> []
    print(sol.zigzagLevelOrder(None))  # Output: []