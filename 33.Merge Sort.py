# Time complexity O(nlogn) | Space complexity O(n)

def merge_sort(arr):
    """Sorts an array using the merge sort algorithm.

    Args:
        arr: The input array to be sorted.

    Returns:
        A new sorted array (original array remains unchanged).
    """
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves and return
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """Merges two sorted arrays into one sorted array.

    Args:
        left: First sorted array
        right: Second sorted array

    Returns:
        A new merged and sorted array containing all elements from both inputs.
    """
    result = []
    i = j = 0  # Initialize pointers for both arrays

    # Compare elements from both arrays and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from either array (one of these will be empty)
    result.extend(left[i:])
    result.extend(right[j:])

    return result
