# Time complexity O(n^2) | Space complexity O(n)

def create_point_set( points):
        """
        Converts a list of [x,y] points into a set of string representations.
        This allows for O(1) lookups when checking if points exist.

        Args:
            points: List of [x,y] coordinate pairs

        Returns:
            A set of strings in "x:y" format representing all points
        """
        point_set = set()
        for point in points:
            x, y = point
            point_string = convert_point_to_string(x, y)
            point_set.add(point_string)
        return point_set

def convert_point_to_string( x, y):
    """
    Helper function to convert x,y coordinates to a consistent string format.
    Using "x:y" format ensures unique representation for each point.
    
    Args:
        x: x-coordinate
        y: y-coordinate
        
    Returns:
        String in "x:y" format
    """
    return str(x) + ":" + str(y)

def minAreaRect( points):
    """
    Finds the minimum area rectangle formed by the given points where sides are 
    parallel to the x and y axes. Returns 0 if no such rectangle exists.
    
    Approach:
    1. Store all points in a hash set for O(1) lookups
    2. Check all possible pairs of points as potential rectangle diagonals
    3. For each diagonal pair, verify if the complementary points exist
    4. Track the minimum valid rectangle area found
    
    Args:
        points: List of [x,y] coordinate pairs
        
    Returns:
        Minimum area rectangle found, or 0 if none exists
    """
    # Create a set of all points for O(1) existence checks
    point_set = create_point_set(points)
    
    # Initialize with infinity so any valid rectangle will be smaller
    minimum_area_found = float('inf')
    
    # Compare each point with all previous points to find diagonal pairs
    for current_index, point2 in enumerate(points):
        point2x, point2y = point2
        
        # Only check against points we've already processed to avoid duplicates
        for previous_index in range(current_index):
            point1x, point1y = points[previous_index]
            
            # Skip if points share an x or y coordinate (can't form diagonal)
            if point1x == point2x or point1y == point2y:
                continue
            
            # Check if the other two points needed to complete the rectangle exist
            point1_on_opposite_diagonal_exists = convert_point_to_string(
                point1x, point2y) in point_set
            point2_on_opposite_diagonal_exists = convert_point_to_string(
                point2x, point1y) in point_set
            
            # If both complementary points exist, we have a valid rectangle
            opposite_diagonal_exists = (point1_on_opposite_diagonal_exists and 
                                        point2_on_opposite_diagonal_exists)
            
            if opposite_diagonal_exists:
                # Calculate area and track the minimum found
                current_area = abs(point2x - point1x) * abs(point2y - point1y)
                minimum_area_found = min(minimum_area_found, current_area)
    
    # Return the minimum area found, or 0 if no rectangle exists
    return minimum_area_found if minimum_area_found != float('inf') else 0