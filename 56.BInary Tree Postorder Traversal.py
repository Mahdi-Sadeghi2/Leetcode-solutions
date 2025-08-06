# Time complexity O(n) | Space complexity O(logn)

def postorderTraversal(root):
    def traverse(node, result):
        if node:
            traverse(node.left, result)  # First recurse on left child
            traverse(node.right, result)  # Then recurse on right child
            result.append(node.val)  # Finally process current node

    result = []
    traverse(root, result)
    return result
