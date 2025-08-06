# Time complexity O(n) | Space complexity O(n)

def inorderTraversal(root):

    def dfs(node, result):
        if node:
            # Traverse left subtree first
            dfs(node.left, result)
            # Visit current node
            result.append(node.val)
            # Traverse right subtree last
            dfs(node.right, result)

    result = []  # Stores the traversal output
    dfs(root, result)
    return result
