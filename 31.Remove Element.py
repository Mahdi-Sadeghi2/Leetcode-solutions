# Time complexity O(n) | Space complexity O(1)

def removeElement(nums, val):
    """
    Removes all instances of 'val' from the list 'nums' in-place and returns the new length.
    Uses a two-pointer approach where elements equal to 'val' are moved to the end of the list.

    Args:
        nums: List of integers to modify (sortedness not required)
        val: Value to remove from the list

    Returns:
        The new length of the list after removal
    """

    # Initialize two pointers:
    # - i starts at the beginning (left pointer)
    # - j starts at the end (right pointer)
    i = 0
    j = len(nums) - 1

    # Process the list while the pointers haven't crossed
    while i <= j:
        if nums[i] == val:
            # If current element matches val, swap it with the element at j
            # This moves the unwanted value to the end of the list
            nums[i], nums[j] = nums[j], nums[i]
            # Decrement j since we've now placed a 'val' at the end
            j -= 1
        else:
            # Current element is valid, move i forward
            i += 1

    # 'i' now represents the count of elements that are not 'val'
    # All elements after index i-1 are either 'val' or were swapped with 'val'
    return i
