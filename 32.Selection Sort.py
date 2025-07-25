# Time complexity O(n^2) | Space complexity O(1)

def selection_sort(nums):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Selection Sort works by repeatedly finding the minimum element from the
    unsorted part of the list and swapping it with the first unsorted element.

    Args:
        nums: List of elements to be sorted (in-place)

    Returns:
        The sorted list (though sorting is done in-place)
    """

    # Outer loop: Traverse through all array elements
    for i in range(len(nums)):
        # Assume the current position is where the minimum should be
        smallest = i

        # Inner loop: Find the minimum element in the remaining unsorted array
        # We start from i+1 because elements before i are already sorted
        for j in range(i+1, len(nums)):
            # If we find an element smaller than our current minimum
            if nums[j] < nums[smallest]:
                smallest = j  # Update the index of the smallest element

        # Swap the found minimum element with the first unsorted element
        # We only swap if we actually found a smaller element
        if i != smallest:
            # Pythonic way to swap two elements
            nums[i], nums[smallest] = nums[smallest], nums[i]

    return nums


print(selection_sort([4, 3, 2, 1, 6, 0, 5]))
