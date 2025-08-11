# Time complexity O(n) | Space complexity O(n)

from collections import deque


def levelOrder(root):
    # Edge case: if tree is empty, return empty list
    if not root:
        return []

    # Initialize result list to store levels
    result = []
    # Use a queue for BFS, starting with root node
    queue = deque([root])

    # Process tree level by level
    while queue:
        # Get number of nodes at current level
        level_size = len(queue)
        # Temporary list to store current level's values
        current_level = []

        # Process all nodes at current level
        for _ in range(level_size):
            # Get next node from front of queue
            node = queue.popleft()
            # Add node's value to current level
            current_level.append(node.val)

            # Add left child to queue if exists
            if node.left:
                queue.append(node.left)
            # Add right child to queue if exists
            if node.right:
                queue.append(node.right)

        # Add current level's values to final result
        result.append(current_level)

    # Return the level order traversal
    return result
