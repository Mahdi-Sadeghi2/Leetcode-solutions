# Time Complexity O(m * n * k) | Space Complexity O(m * n * k)
from collections import deque


class Solution:
    def shortestPath(grid, k):
        m, n = len(grid), len(grid[0])

        # If the grid is 1x1, no steps are needed
        if m == 1 and n == 1:
            return 0

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Queue for BFS: elements are tuples of (row, column, remaining_k, steps)
        queue = deque([(0, 0, k, 0)])

        # Visited dictionary: key = (row, column), value = max remaining k
        visited = {}
        visited[(0, 0)] = k

        while queue:
            i, j, remaining_k, steps = queue.popleft()

            # Explore all four possible directions
            for di, dj in directions:
                ni, nj = i + di, j + dj

                # Check if the new position is within grid bounds
                if 0 <= ni < m and 0 <= nj < n:
                    # Calculate new remaining k after moving to (ni, nj)
                    new_k = remaining_k - grid[ni][nj]

                    # If we can eliminate the obstacle or it's an empty cell
                    if new_k >= 0:
                        # Check if we've reached the destination
                        if ni == m - 1 and nj == n - 1:
                            return steps + 1

                        # If this cell hasn't been visited or can be visited with more remaining k
                        if (ni, nj) not in visited or new_k > visited[(ni, nj)]:
                            visited[(ni, nj)] = new_k
                            queue.append((ni, nj, new_k, steps + 1))

        # If the destination wasn't reached
        return -1
