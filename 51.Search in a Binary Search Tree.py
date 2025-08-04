# Time complexity O(logn) | Space complexity O(1)

def searchBST(root, val: int):
    # Start from the root of the tree
    current = root

    # Traverse the tree while current node exists
    while current:
        # If the value matches, return the current node
        if val == current.val:
            return current

        # If the target value is smaller, search in the left subtree
        elif val < current.val:
            current = current.left

        # If the target value is larger, search in the right subtree
        else:
            current = current.right

    # Value not found, return None
    return None
