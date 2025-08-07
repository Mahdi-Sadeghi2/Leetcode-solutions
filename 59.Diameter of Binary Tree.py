# Time complexity O(n) | Space complexity O(n)


def diameterOfBinaryTree(root):
    if not root:
        return 0  # Empty tree has diameter 0

    max_diameter = 0  # Tracks the maximum diameter found during traversal

    def dfs(node):
        
        nonlocal max_diameter  # Allows modifying the outer max_diameter

        if not node:
            # Base case: height of an empty subtree is -1 (adjusts for edge counting)
            return -1

        # Recursively get heights of left and right subtrees
        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # Calculate the diameter passing through the current node
        current_diameter = left_height + right_height + \
            2  # +2 for edges from node to left/right
        # Update global maximum
        max_diameter = max(max_diameter, current_diameter)

        # Return the height of the current subtree
        # +1 for the current node's edge
        return max(left_height, right_height) + 1

    dfs(root)  # Start DFS from the root
    return max_diameter
