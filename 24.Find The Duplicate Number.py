# Time complexity O(n) | Space complexity O(1)

def findDuplicate(nums):
    # Traverse each element in the array
    for value in nums:
        # Use the absolute value to handle possible negative markings
        abs_value = abs(value)

        # Check if the value at position (abs_value - 1) is already negative
        # If yes, it means we've seen abs_value before (it's a duplicate)
        if nums[abs_value - 1] < 0:
            return abs_value  # Return the duplicate value

        # Mark the value at position (abs_value - 1) as visited by making it negative
        nums[abs_value - 1] *= -1

    # If no duplicates found, return -1 (though problem states there's at least one)
    return -1
