# Time complexity O(h + k) | Space complexity O(h)

def kthSmallest(root, k: int) -> int:
    stack = []          # Stack to simulate recursion and track nodes
    current = root      # Pointer to traverse the tree
    count = 0           # Counter to track the number of visited nodes

    # Continue traversal while there are nodes to process
    while stack or current:
        # Traverse to the leftmost node (smallest element)
        while current:
            stack.append(current)  # Push nodes onto the stack as we go left
            current = current.left

        # Process the node at the top of the stack (in-order)
        current = stack.pop()     # Visit the smallest remaining node
        count += 1                # Increment the visited node count

        # If we've reached the k-th smallest, return its value
        if count == k:
            return current.val

        # Move to the right subtree to continue traversal
        current = current.right

    # Return -1 if k is larger than the number of nodes (edge case)
    return -1
