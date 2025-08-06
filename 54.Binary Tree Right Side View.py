# Time complexity O(n) | Space complexity O(n)


from collections import deque
from typing import Optional, List


def rightSideView(root) -> List[int]:
    # Edge case: If the tree is empty, return an empty list
    if not root:
        return []

    # Initialize a list to store the rightmost nodes at each level
    right_view = []
    # Use a queue for BFS (level-order traversal), starting with the root node
    queue = deque([root])

    # Process each level of the tree
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)

        # Iterate through all nodes at the current level
        for i in range(level_size):
            # Remove the front node from the queue
            node = queue.popleft()

            # If this is the last node in the current level, add its value to the result
            # (This is the rightmost node visible from the right side)
            if i == level_size - 1:
                right_view.append(node.val)

            # Add the left child to the queue if it exists
            if node.left:
                queue.append(node.left)
            # Add the right child to the queue if it exists
            if node.right:
                queue.append(node.right)

    # Return the list of rightmost nodes at each level
    return right_view
