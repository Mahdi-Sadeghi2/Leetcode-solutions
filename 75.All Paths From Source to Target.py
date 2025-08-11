# Time Complexity O(2^n*n) | Space Complexity O(n)

def allPathsSourceTarget(graph):
    def backtrack(node, path):
        # If the current node is the target, add the current path to the result
        if node == target:
            result.append(path.copy())
            return
        # Explore each neighbor of the current node
        for neighbor in graph[node]:
            path.append(neighbor)  # Move to the neighbor
            backtrack(neighbor, path)  # Recursively explore further
            path.pop()  # Backtrack to explore other neighbors

    target = len(graph) - 1  # The target node is the last node in the graph
    result = []  # Store all valid paths from source to target
    backtrack(0, [0])  # Start backtracking from node 0 with initial path [0]
    return result
