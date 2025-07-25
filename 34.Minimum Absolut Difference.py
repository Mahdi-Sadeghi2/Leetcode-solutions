# Time complexity O(nlogn) | Space complexity O(n)


def minimumAbsDifference(arr):
    # Sort the array to ensure adjacent elements have the smallest possible differences
    arr.sort()

    # Initialize minimum difference as infinity (to be updated later)
    min_difference = float('inf')
    # This will store all pairs with the minimum difference
    result = []

    # First pass: Find the minimum absolute difference
    for i in range(1, len(arr)):
        # Calculate the difference between current and previous element
        difference = arr[i] - arr[i-1]

        # Update min_difference if we find a smaller difference
        if difference < min_difference:
            min_difference = difference

    # Second pass: Collect all pairs that have the minimum difference
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_difference:
            # Append the pair to the result list
            result.append([arr[i-1], arr[i]])

    return result
