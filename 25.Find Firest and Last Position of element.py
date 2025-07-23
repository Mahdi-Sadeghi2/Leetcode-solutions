# Time complexity O(logn) | Space complexity O(1)

def find_left_extreme(nums, target):
    """
    Finds the first occurrence (leftmost index) of target in a sorted array nums.
    Returns -1 if target is not found.
    Uses binary search for O(log n) time complexity.
    """
    left = 0
    right = len(nums)-1

    while (left <= right):
        middle = (left + right)//2

        if nums[middle] == target:
            # Check if we've found the leftmost occurrence
            if middle == 0:  # If at start of array, must be leftmost
                return 0
            elif nums[middle-1] == target:  # If previous element is also target, search left half
                right = middle - 1
            else:  # Previous element is different, so this is leftmost
                return middle
        elif target < nums[middle]:
            right = middle-1  # Target is in left half
        else:
            left = middle+1  # Target is in right half

    return -1  # Target not found


def find_right_extreme(nums, target):
    """
    Finds the last occurrence (rightmost index) of target in a sorted array nums.
    Returns -1 if target is not found.
    Uses binary search for O(log n) time complexity.
    """
    left = 0
    right = len(nums)-1

    while (left <= right):
        middle = (left + right)//2

        if nums[middle] == target:
            # Check if we've found the rightmost occurrence
            if middle == len(nums)-1:  # If at end of array, must be rightmost
                return middle
            elif nums[middle+1] == target:  # If next element is also target, search right half
                left = middle + 1
            else:  # Next element is different, so this is rightmost
                return middle
        elif target < nums[middle]:
            right = middle-1  # Target is in left half
        else:
            left = middle+1  # Target is in right half

    return -1  # Target not found


def searchRange(nums, target):
    """
    Returns the starting and ending position of a given target value in a sorted array.
    If target is not found, returns [-1, -1].

    Args:
    nums: List[int] - a sorted array of integers
    target: int - the value to search for

    Returns:
    List[int] - first and last indices of target in nums
    """
    left_extreme = find_left_extreme(nums, target)  # Find first occurrence
    right_extreme = find_right_extreme(nums, target)  # Find last occurrence
    return [left_extreme, right_extreme]
