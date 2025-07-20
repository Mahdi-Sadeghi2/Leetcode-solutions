# Time complexity O(n) | Space complexity O(n)

def findDiagonalOrder(mat):
    """
    Traverse a 2D matrix in diagonal zigzag (snake) order.
    :type mat: List[List[int]]
    """
    # Handle empty matrix case
    if not mat or not mat[0]:
        return []

    # Get matrix boundaries (0-based indices)
    height = len(mat)-1  # Last row index
    width = len(mat[0])-1  # Last column index
    result = []  # Stores the traversal order

    # Start at top-left corner (0,0)
    row, col = 0, 0

    # Direction flag: False = moving up-right, True = moving down-left
    going_down = False  # Start with upward direction

    def is_out_of_bounds(row, col, height, width):
        """Check if current position is outside matrix boundaries"""
        return row < 0 or row > height or col < 0 or col > width

    # Continue until we traverse all elements
    while not is_out_of_bounds(row, col, height, width):
        result.append(mat[row][col])  # Add current element to result

        if going_down:
            # When moving down-left
            if col == 0 or row == height:
                # Hit left border or bottom border - change direction
                going_down = False
                if row == height:
                    # At bottom, move right
                    col += 1
                else:
                    # At left border, move down
                    row += 1
            else:
                # Continue moving down-left
                row += 1
                col -= 1
        else:
            # When moving up-right
            if row == 0 or col == width:
                # Hit top border or right border - change direction
                going_down = True
                if col == width:
                    # At right border, move down
                    row += 1
                else:
                    # At top border, move right
                    col += 1
            else:
                # Continue moving up-right
                row -= 1
                col += 1

    return result
