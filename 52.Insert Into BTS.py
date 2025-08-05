# Time complexity O(logn) | Space complexity O(logn)
def insertIntoBST(root, val: int):
    # Base case: If tree is empty, create new node
    if not root:
        return TreeNode(val)

    # If value is less than current node's value, insert into left subtree
    if val < root.val:
        root.left = insertIntoBST(root.left, val)

    # If value is greater than current node's value, insert into right subtree
    else:
        root.right = insertIntoBST(root.right, val)

    # Return the (potentially modified) root node
    return root
