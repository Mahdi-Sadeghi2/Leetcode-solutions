# Time complexity O(n^2) | Space complexity O(n)


def maxPoints(points):
    """
    Given a list of 2D points, returns the maximum number of points that lie on the same straight line.
    Approach:
    1. For each point, calculate slopes with all other points
    2. Use GCD to represent slopes in reduced form to avoid floating point precision issues
    3. Count points sharing the same slope (plus duplicates)
    4. Track the maximum count found
    """

    def get_slope_of_line_between_points(point_one, point_two):
        """
        Calculates the slope between two points as a reduced fraction [numerator, denominator].
        Returns [1, 0] for vertical lines (infinite slope).
        """
        point_one_axis_x, point_one_axis_y = point_one
        point_two_axis_x, point_two_axis_y = point_two
        slope = [1, 0]  # Default for vertical lines

        if point_one_axis_x != point_two_axis_x:
            # Calculate differences in x and y coordinates
            difference_axis_x = point_two_axis_x - point_one_axis_x
            difference_axis_y = point_two_axis_y - point_one_axis_y

            # Reduce slope to simplest form using GCD
            greatest_common_deviser = get_greatest_common_deviser(
                abs(difference_axis_x), abs(difference_axis_y))

            difference_axis_x = difference_axis_x // greatest_common_deviser
            difference_axis_y = difference_axis_y // greatest_common_deviser

            # Ensure consistent representation of negative slopes
            if difference_axis_x < 0:
                difference_axis_x *= -1
                difference_axis_y *= -1
            # Slope as [rise, run]
            slope = [difference_axis_y, difference_axis_x]
        return slope

    def create_hash_able_key_for_rational(numerator, denominator):
        """Creates a string key from slope components to use in hash map"""
        return str(numerator) + ":" + str(denominator)

    def get_greatest_common_deviser(num1, num2):
        """Calculates GCD using Euclidean algorithm"""
        a, b = abs(num1), abs(num2)
        while b:
            a, b = b, a % b
        return a

    # Edge case: 0-2 points are always colinear
    if len(points) <= 2:
        return len(points)

    max_number_of_points_on_line = 1  # Minimum possible for distinct points

    # Compare each point with all other points
    for index_one, point_one in enumerate(points):
        slopes = {}  # Tracks count of points for each slope
        duplicate_points = 1  # Counts the current point and its duplicates

        for index_two in range(index_one + 1, len(points)):
            point_two = points[index_two]

            # Handle duplicate points
            if point_one == point_two:
                duplicate_points += 1
                continue

            # Calculate slope and create a hash key
            rise, run = get_slope_of_line_between_points(point_one, point_two)
            slope_key = create_hash_able_key_for_rational(rise, run)

            # Update count for this slope
            if slope_key not in slopes:
                slopes[slope_key] = 0
            slopes[slope_key] += 1

        # Calculate maximum points on any line through point_one
        current_max = duplicate_points  # Start with duplicate count
        if slopes:  # Only try max() if slopes exist (Python 2 compatibility)
            current_max += max(slopes.values())

        # Update global maximum
        max_number_of_points_on_line = max(
            max_number_of_points_on_line, current_max)

    return max_number_of_points_on_line
