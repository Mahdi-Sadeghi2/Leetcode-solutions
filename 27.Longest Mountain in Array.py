# Time complexity O(n) | Space complexity O(1)

def longestMountain(arr):
    """
    Finds the length of the longest 'mountain' (peak) in an array.
    A mountain is defined as a subarray where:
    - Elements strictly increase to a peak, then
    - Elements strictly decrease after the peak.
    The mountain must have at least 3 elements.

    Args:
        arr (List[int]): Input array of integers.

    Returns:
        int: Length of the longest mountain (0 if none found).
    """

    longest_peak_length = 0  # Track the longest mountain found
    i = 1  # Start from the second element (peaks cannot be at edges)

    while i < len(arr) - 1:  # Avoid edge cases (peaks need left & right neighbors)
        # Check if current element is a peak (greater than both neighbors)
        is_peak = arr[i-1] < arr[i] and arr[i] > arr[i+1]

        if not is_peak:
            i += 1  # Not a peak, move to the next element
            continue

        # Expand to the left to find the start of the increasing sequence
        left_index = i - 2  # Start checking from the element before the left neighbor
        while left_index >= 0 and arr[left_index] < arr[left_index + 1]:
            left_index -= 1  # Move left while the sequence is increasing

        # Expand to the right to find the end of the decreasing sequence
        right_index = i + 2  # Start checking from the element after the right neighbor
        while right_index < len(arr) and arr[right_index] < arr[right_index - 1]:
            right_index += 1  # Move right while the sequence is decreasing

        # Calculate the current mountain length
        # -1 to convert indices to length
        current_peak_length = right_index - left_index - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)

        # Skip the already processed decreasing part (optimization)
        i = right_index

    return longest_peak_length
