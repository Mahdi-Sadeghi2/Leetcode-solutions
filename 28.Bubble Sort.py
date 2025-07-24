# Time complexity O(n) | space complexity O(1)

def sortArray(nums):
    """
    Sorts an array in ascending order using Bubble Sort.
    Args:
        nums (list): The input array to be sorted.
    Returns:
        list: The sorted array.
    """

    # Initialize a flag to track if the array is sorted
    sorted_nums = False
    # Counter to optimize by reducing the inner loop range each pass
    counter = 0

    # Continue looping until no swaps are made in a full pass
    while not sorted_nums:
        sorted_nums = True  # Assume the array is sorted until a swap occurs

        # Iterate through the unsorted portion of the array
        for i in range(len(nums) - 1 - counter):
            # If current element > next element, swap them
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Mark that a swap occurred (array not yet sorted)
                sorted_nums = False

        # After each pass, the largest unsorted element "bubbles up" to its correct position
        counter += 1

    return nums
