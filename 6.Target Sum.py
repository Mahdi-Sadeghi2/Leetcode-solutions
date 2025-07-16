# Time complexity O(n^2) | Space complexity O(n)


def findTargetSumWays(nums, target):
    # Initialize a dictionary to keep track of the number of ways to achieve each sum
    # Start with 0 sum, which can be achieved in 1 way (by not selecting any numbers)
    reuslt = {0: 1}

    # Iterate through each number in the input array
    for num in nums:
        # Create a new dictionary to store the updated sums after processing the current number
        new_reuslt = {}

        # For each existing sum in the current reuslt dictionary
        for current_sum in reuslt:
            # Add the current number to the existing sum
            new_sum = current_sum + num
            # Update the count in new_reuslt for the new_sum
            if new_sum in new_reuslt:
                new_reuslt[new_sum] += reuslt[current_sum]
            else:
                new_reuslt[new_sum] = reuslt[current_sum]

            # Subtract the current number from the existing sum
            new_sum = current_sum - num
            # Update the count in new_reuslt for the new_sum
            if new_sum in new_reuslt:
                new_reuslt[new_sum] += reuslt[current_sum]
            else:
                new_reuslt[new_sum] = reuslt[current_sum]

        # Update reuslt to new_reuslt for the next iteration
        reuslt = new_reuslt

    # The result is the number of ways to achieve the target sum, default to 0 if target is not found
    return reuslt.get(target, 0)


print(findTargetSumWays([1, 1, 1, 1, 1], 3))
