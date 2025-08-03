# Time complexity O(MNlog(MN)) | Space complexity O(MN)
import heapq


def trapRainWater(heightMap):
    # Edge case: empty grid
    if not heightMap or not heightMap[0]:
        return 0

    # Get dimensions of the grid
    m, n = len(heightMap), len(heightMap[0])

    # Min-heap to always process the lowest boundary next
    heap = []

    # Visited matrix to track processed cells
    visited = [[False for _ in range(n)] for _ in range(m)]

    # Step 1: Push all boundary cells into the heap
    # Process left and right columns
    for i in range(m):
        for j in [0, n-1]:
            heapq.heappush(heap, (heightMap[i][j], i, j))
            visited[i][j] = True
    # Process top and bottom rows (excluding corners already processed)
    for j in range(n):
        for i in [0, m-1]:
            heapq.heappush(heap, (heightMap[i][j], i, j))
            visited[i][j] = True

    # Possible movement directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    total_water = 0

    # Step 2: Process cells from the heap
    while heap:
        current_height, x, y = heapq.heappop(heap)

        # Explore all 4 neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if neighbor is within bounds and not visited
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                neighbor_height = heightMap[nx][ny]

                # If neighbor is lower than current boundary, water can be trapped
                if neighbor_height < current_height:
                    total_water += current_height - neighbor_height

                # Mark neighbor as visited and add to heap with new boundary height
                visited[nx][ny] = True
                # The new boundary is the max between current and neighbor height
                heapq.heappush(
                    heap, (max(current_height, neighbor_height), nx, ny))

    return total_water
