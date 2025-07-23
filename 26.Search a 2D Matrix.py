# Time complexity O(logmn) | Space complexity O(1)

def searchMatrix(matrix, target):
    """
    Searches for a target value in a 2D matrix where:
    - Each row is sorted in ascending order
    - The first element of each row is greater than the last element of the previous row

    Uses binary search to first identify the correct row, then searches within that row.

    Args:
        matrix (List[List[int]]): The 2D matrix to search in
        target (int): The value to search for

    Returns:
        bool: True if target is found, False otherwise
    """
    columns = len(matrix[0])  # Number of columns in the matrix
    rows = len(matrix)        # Number of rows in the matrix

    # Binary search to identify the relevant row that could contain the target
    top = 0
    bottom = rows - 1
    while (top <= bottom):
        middle = (top + bottom) // 2

        # If target is smaller than the first element in the middle row,
        # it must be in a row above
        if target < matrix[middle][0]:
            bottom = middle - 1

        # If target is larger than the last element in the middle row,
        # it must be in a row below
        elif target > matrix[middle][columns - 1]:
            top = middle + 1

        # Otherwise, the target is within this row
        else:
            break

    # If top > bottom, the target is not in any row
    if top > bottom:
        return False

    # Now perform binary search within the identified row
    left = 0
    right = columns - 1
    while (left <= right):
        middle_value = (left + right) // 2

        # Check if the middle element is the target
        if target == matrix[middle][middle_value]:
            return True

        # If target is smaller, search the left half
        elif target < matrix[middle][middle_value]:
            right = middle_value - 1

        # If target is larger, search the right half
        else:
            left = middle_value + 1

    # If not found in the row, return False
    return False
