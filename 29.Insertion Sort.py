# Time complexity O(n^2) | Space complexity O(1)

def insertion_sort(nums):
    """
    Sorts a list of numbers in ascending order using Insertion Sort algorithm.
    
    Args:
        nums (list): The list of numbers to be sorted.
        
    Returns:
        list: The sorted list in ascending order.
    """

    # Start from the second element (index 1) since the first element is trivially sorted
    for i in range(1, len(nums)):
        # Store the current element to be inserted
        current = nums[i]
        # Start comparing with the previous element
        j = i - 1

        # Shift elements of the sorted segment that are greater than 'current'
        # to the right to make space for insertion
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]  # Move the larger element one position ahead
            j -= 1  # Move backwards through the sorted segment

        # Insert the 'current' element into its correct position
        nums[j + 1] = current

    return nums
