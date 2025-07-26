# Time complexity O(n) | Space complexity O(n)

def spiralOrder(matrix):
    # Handle empty matrix case
    if not matrix or not matrix[0]:
        return []

    result = []
    # Initialize boundaries:
    # start_row: top boundary, end_row: bottom boundary
    # start_col: left boundary, end_col: right boundary
    start_row, end_row = 0, len(matrix)-1
    start_col, end_col = 0, len(matrix[0])-1

    # Continue while boundaries haven't crossed
    while start_row <= end_row and start_col <= end_col:
        # Traverse from left to right along top boundary
        for col in range(start_col, end_col+1):
            result.append(matrix[start_row][col])
        # Move top boundary down one row
        start_row += 1

        # Traverse from top to bottom along right boundary
        for row in range(start_row, end_row+1):
            result.append(matrix[row][end_col])
        # Move right boundary left one column
        end_col -= 1

        # If we still have rows to traverse (for non-square matrices)
        if start_row <= end_row:
            # Traverse from right to left along bottom boundary
            for col in reversed(range(start_col, end_col+1)):
                result.append(matrix[end_row][col])
            # Move bottom boundary up one row
            end_row -= 1

        # If we still have columns to traverse (for non-square matrices)
        if start_col <= end_col:
            # Traverse from bottom to top along left boundary
            for row in reversed(range(start_row, end_row+1)):
                result.append(matrix[row][start_col])
            # Move left boundary right one column
            start_col += 1

    return result
