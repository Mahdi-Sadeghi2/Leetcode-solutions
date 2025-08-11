# Time complexity O(n+e) | Space complexity O(n)


from collections import deque


def cloneGraph(node):
    if not node:
        return None

    # Dictionary to map original nodes to their clones
    clone_map = {}

    # Initialize the queue with the original node
    queue = deque([node])

    # Create the clone of the starting node
    clone_map[node] = Node(node.val)

    while queue:
        current_node = queue.popleft()

        for neighbor in current_node.neighbors:
            if neighbor not in clone_map:
                # Clone the neighbor if not already cloned
                clone_map[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            # Add the cloned neighbor to the current clone's neighbors
            clone_map[current_node].neighbors.append(clone_map[neighbor])

    return clone_map[node]
