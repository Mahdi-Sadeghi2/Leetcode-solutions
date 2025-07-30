# Time complexity O(n) | Space compelxity O(1)

def checkStraightLine(coordinates):
    """
    Determines if all given coordinates lie on a straight line.

    Args:
        coordinates (List[List[int]]): A list of [x, y] coordinate pairs.

    Returns:
        bool: True if all points are colinear, False otherwise.
    """
    # Edge case: 0, 1, or 2 points are always colinear
    if len(coordinates) <= 2:
        return True

    # Extract the first two points to determine the reference line
    x0, y0 = coordinates[0]  # First point (reference point)
    x1, y1 = coordinates[1]  # Second point (to calculate initial slope)

    # Calculate the differences in x and y between the first two points
    # These represent the 'run' (dx) and 'rise' (dy) of the line
    dx = x1 - x0
    dy = y1 - y0

    # Check all remaining points to see if they lie on the same line
    for i in range(2, len(coordinates)):
        xi, yi = coordinates[i]  # Current point being checked

        # To avoid division (and handle vertical lines), we use cross-multiplication:
        # If three points (x0,y0), (x1,y1), (xi,yi) are colinear, then:
        # (y1 - y0)/(x1 - x0) = (yi - y0)/(xi - x0)
        # Which can be rewritten as:
        # (y1 - y0) * (xi - x0) = (yi - y0) * (x1 - x0)
        # Or in our variables: dy*(xi - x0) == (yi - y0)*dx
        if (yi - y0) * dx != (xi - x0) * dy:
            return False  # Point doesn't lie on the line

    # All points passed the colinearity check
    return True
