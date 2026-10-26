# 71. Simplify Path (Medium)
# Time Complexity: O(N) | Space Complexity: O(N)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')

        for comp in components:
            if comp == '..':
                if stack:
                    stack.pop()
            elif comp and comp != '.':
                stack.append(comp)

        return '/' + '/'.join(stack)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.simplifyPath("/home/"))                 # Output: "/home"

    # Example 2
    print(sol.simplifyPath("/home//foo/"))            # Output: "/home/foo"

    # Example 3
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))  # Output: "/home/user/Pictures"

    # Example 4
    print(sol.simplifyPath("/../"))                   # Output: "/"

    # Example 5
    print(sol.simplifyPath("/.../a/../b/c/../d/./"))    # Output: "/.../b/d"
    