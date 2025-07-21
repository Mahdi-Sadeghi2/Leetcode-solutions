# Time complexity O(n) | Space complexity O(n) (excluding output array)
def productExceptSelf(nums):
    # Initialize the output array with 1's (since product = left * right, and initially left/right are 1)
    products = [1 for _ in range(len(nums))]

    # --- LEFT PASS ---
    # Compute the product of all elements to the LEFT of each index
    left_running_product = 1  # Initialize left product accumulator
    for i in range(len(nums)):
        # Store the product of all elements before nums[i]
        products[i] = left_running_product
        # Update the running product to include nums[i] for the next iteration
        left_running_product *= nums[i]

    # --- RIGHT PASS ---
    # Now compute the product of all elements to the RIGHT and multiply with the left product
    right_running_product = 1  # Initialize right product accumulator
    for i in reversed(range(len(nums))):
        # Multiply the existing left product with the right product
        products[i] *= right_running_product
        # Update the running product to include nums[i] for the next iteration
        right_running_product *= nums[i]

    return products
