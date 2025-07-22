# Time complexity O(logn) | Space complexity O(1)

def search(nums, target):
    # Initialize pointers for binary search
    left = 0
    right = len(nums)-1

    # Continue searching while the search space is valid
    while (left <= right):
        # Calculate the middle index
        middle = (left+right)//2

        # If target is found at middle, return immediately
        if nums[middle] == target:
            return middle

        # Check if the left half [left..middle] is sorted
        if nums[left] <= nums[middle]:
            # Left half is sorted

            # If target is within the sorted left half's range
            if target >= nums[left] and target < nums[middle]:
                # Narrow search to the left half
                right = middle-1
            else:
                # Otherwise search the right half
                left = middle+1
        else:
            # Right half [middle..right] is sorted

            # If target is within the sorted right half's range
            if target <= nums[right] and target > nums[middle]:
                # Narrow search to the right half
                left = middle+1
            else:
                # Otherwise search the left half
                right = middle-1

    # Target not found in the array
    return -1
