# Time complexity O(n) | Space complexity O(1)
def maxArea(height):
    # Initialize maximum area to 0
    area = 0

    # Left pointer starts at the beginning of the array
    i = 0

    # Right pointer starts at the end of the array
    j = len(height) - 1

    # Two-pointer approach: move the pointer pointing to the shorter line inward
    while (i < j):
        # The height of the container is limited by the shorter line
        h = min(height[i], height[j])

        # Calculate the area between the two lines
        new_area = h * (j - i)

        # Update the maximum area found so far
        area = max(area, new_area)

        # Move the pointer pointing to the shorter line inward,
        # as keeping the taller line might lead to a larger area
        if (height[i] < height[j]):
            i += 1
        else:
            j -= 1

    return area
