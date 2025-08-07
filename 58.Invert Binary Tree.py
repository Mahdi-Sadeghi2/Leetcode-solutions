# Time complexity O(n) | Space complexity O(n)

from collections import deque


def invertTree(root):
   # Edge case: If the tree is empty, return None
    if root is None:
        return None

    # Initialize a queue for BFS and add the root node
    queue = deque([root])

    # Process nodes level by level
    while queue:
        # Dequeue the front node
        current = queue.popleft()

        # Swap left and right children of the current node
        current.left, current.right = current.right, current.left

        # Enqueue left child if it exists (for further processing)
        if current.left:
            queue.append(current.left)

        # Enqueue right child if it exists (for further processing)
        if current.right:
            queue.append(current.right)

    # Return the root of the inverted tree
    return root
