# Time complexity O(m*n) | Space complexity O(m*n)

from collections import deque

from collections import deque


def floodFill(image, sr, sc, color):
    # Store the original color of the starting pixel
    original_color = image[sr][sc]

    # If the starting pixel is already the target color, no changes needed
    if original_color == color:
        return image

    # Get the dimensions of the image (rows and columns)
    rows, cols = len(image), len(image[0])

    # Initialize a queue for BFS and add the starting position (sr, sc)
    queue = deque([(sr, sc)])

    # Change the starting pixel to the new color
    image[sr][sc] = color

    # Define 4-directional movements: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Perform BFS to fill connected pixels
    while queue:
        # Get the current pixel position (row, column)
        r, c = queue.popleft()

        # Check all 4 neighboring pixels
        for dr, dc in directions:
            # Compute the new position (nr, nc)
            nr, nc = r + dr, c + dc

            # Check if the new position is within bounds and has the original color
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                # Update the pixel to the new color
                image[nr][nc] = color

                # Add the new position to the queue for further processing
                queue.append((nr, nc))

    # Return the modified image after flood fill
    return image
