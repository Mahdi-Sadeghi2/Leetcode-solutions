# Time complexity O(m*n) | Space complexity O(min(m*n))
from collections import deque



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: If the grid is empty, return 0 islands
        if not grid:
            return 0

        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Initialize the island counter
        num_islands = 0

        # Define 4-directional movements: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Traverse each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # If the cell is land ('1'), start BFS to mark the entire island
                if grid[row][col] == "1":
                    # Increment island count
                    num_islands += 1

                    # Initialize BFS queue with the current land cell
                    queue = deque([(row, col)])

                    # Mark the current cell as visited by setting it to '0'
                    grid[row][col] = "0"

                    # Process all connected land cells using BFS
                    while queue:
                        # Get the current cell coordinates
                        current_row, current_col = queue.popleft()

                        # Check all 4-directional neighbors
                        for dr, dc in directions:
                            # Calculate neighbor coordinates
                            nr, nc = current_row + dr, current_col + dc

                            # Check if neighbor is within bounds and is unvisited land
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                # Mark neighbor as visited
                                grid[nr][nc] = "0"

                                # Add neighbor to the queue for further processing
                                queue.append((nr, nc))

        # Return the total number of islands found
        return num_islands
