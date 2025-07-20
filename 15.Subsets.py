# Time complexity O(2^n*n) | Space complexity(2^n*n)
def subsets(nums):
    # Initialize the output list to store all subsets
    output = []

    # Helper function to generate subsets using backtracking
    def helper(nums, i, subset):
        # Base case: When we've processed all elements, add the current subset to output
        if i == len(nums):
            # Append a COPY of the subset (using subset[:] to avoid reference issues)
            output.append(subset[:])
            return

        # Recursive case 1: Exclude nums[i] - proceed without adding it to the subset
        helper(nums, i + 1, subset)

        # Recursive case 2: Include nums[i] - add it to the subset and proceed
        subset.append(nums[i])
        helper(nums, i + 1, subset)

        # Backtrack: Remove nums[i] to revert subset to its state before inclusion
        # (This allows reuse of the subset list for other recursive branches)
        subset.pop()

    # Start the recursion with the first index (i=0) and an empty subset
    helper(nums, 0, [])

    # Return the list of all generated subsets
    return output
