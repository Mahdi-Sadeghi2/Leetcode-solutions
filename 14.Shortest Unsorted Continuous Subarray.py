# Time complexity O(n) | Space complexity O(1)

def findUnsortedSubarray(nums):
    """
    Finds the length of the shortest continuous subarray that, if sorted, 
    would make the entire array sorted in ascending order.

    """

    def is_out_of_order(i, nums):
        """
        Helper function to check if an element at index i is out of order.

        """
        num = nums[i]
        # For first element, only check if it's greater than next element
        if i == 0:
            # Edge case: single element array
            return num > nums[i+1] if len(nums) > 1 else False
        # For last element, only check if it's smaller than previous element
        if i == len(nums) - 1:
            # Edge case: single element array
            return num < nums[i-1] if len(nums) > 1 else False
        # For middle elements, check both neighbors
        return num > nums[i+1] or num < nums[i-1]

    # Initialize variables to track min and max out-of-order elements
    min_out_of_order = float('inf')  # Start with maximum possible value
    max_out_of_order = float('-inf')  # Start with minimum possible value

    # First pass: Identify all out-of-order elements and find min/max among them
    for i in range(len(nums)):
        if is_out_of_order(i, nums):
            min_out_of_order = min(min_out_of_order, nums[i])
            max_out_of_order = max(max_out_of_order, nums[i])

    # If no elements were out of order, array is already sorted
    if min_out_of_order == float('inf'):
        return 0  # Already sorted

    # Find the correct position for the min_out_of_order in the sorted array
    left = 0
    while left < len(nums) and min_out_of_order >= nums[left]:
        left += 1

    # Find the correct position for the max_out_of_order in the sorted array
    right = len(nums) - 1
    while right >= 0 and max_out_of_order <= nums[right]:
        right -= 1

    # Return the length of the subarray between left and right (inclusive)
    # If right < left, return 0 (edge case where array is already sorted)
    return right - left + 1 if right >= left else 0
