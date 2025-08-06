# Time complexity O(n) | Space complexity O(logn)

def preorderTraversal(root):
    def traverse(node, result):
        if node:
            result.append(node.val)  # Visit root first
            traverse(node.left, result)  # Then left subtree
            traverse(node.right, result)  # Then right subtree

    result = []
    traverse(root, result)
    return result
