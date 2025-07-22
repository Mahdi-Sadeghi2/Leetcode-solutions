# Time complexity O(logn) | Space complexity O(1)

def search(nums, target):
    # Initialize binary search pointers
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2  # Find the middle index

        # Case 1: Found the target
        if nums[middle] == target:
            return middle

        # Case 2: Left half [left..middle] is sorted
        if nums[left] <= nums[middle]:
            # Check if target is within the sorted left half
            if nums[left] <= target < nums[middle]:
                right = middle - 1  # Search left half
            else:
                left = middle + 1    # Search right half

        # Case 3: Right half [middle..right] is sorted
        else:
            # Check if target is within the sorted right half
            if nums[middle] < target <= nums[right]:
                left = middle + 1    # Search right half
            else:
                right = middle - 1   # Search left half

    # Target not found
    return -1
