# Time complexity O(logn) | Space complexity O(1)

def search(nums, target):
    # Initialize left and right pointers to start and end of the list
    left = 0
    right = len(nums)-1

    # Continue searching while the search space is valid (left hasn't passed right)
    while left <= right:
        # Calculate the middle index to divide the search space
        middle = (left+right)//2

        # Check if the middle element is the target
        if nums[middle] == target:
            return middle  # Target found, return its index

        # If target is greater than middle element, search the right half
        elif nums[middle] < target:
            left = middle + 1

        # If target is smaller than middle element, search the left half
        else:
            right = middle - 1

    # If loop ends without finding the target, return -1 (not found)
    return -1
