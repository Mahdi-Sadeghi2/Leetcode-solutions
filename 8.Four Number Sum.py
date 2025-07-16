# Time complexity O(n^2) | Space complexity O(n^2)

def fourSum(nums, target):
   # Sort the array to help with duplicate detection
    nums.sort()

    # Dictionary to store all possible two-sum pairs and their indices
    all_pair_sum = {}

    # List to store found quadruplets (may contain duplicates initially)
    quadruplets = []

    # First loop: iterate through potential third elements (i)
    for i in range(1, len(nums)-1):
        # Second loop: iterate through potential fourth elements (j)
        for j in range(i+1, len(nums)):
            current_sum = nums[i] + nums[j]
            difference = target - current_sum

            # Check if we have pairs that sum to the needed difference
            if difference in all_pair_sum:
                for pair in all_pair_sum[difference]:
                    # Verify all indices are distinct (no element reuse)
                    if i not in [pair[0], pair[1]] and j not in [pair[0], pair[1]]:
                        # Create the quadruplet and store its sorted version
                        quad = list(pair) + [nums[i], nums[j]]
                        quad_sorted = sorted(quad)
                        # Store for later deduplication
                        quadruplets.append(quad_sorted)

        # Store all two-sum pairs that end at current i (as first element)
        for k in range(0, i):
            current_sum = nums[i] + nums[k]
            # Store values for easier reconstruction
            pair_values = (nums[k], nums[i])

            # Add to dictionary if not already present
            if current_sum not in all_pair_sum:
                all_pair_sum[current_sum] = [pair_values]
            else:
                # Avoid storing duplicate pairs
                if pair_values not in all_pair_sum[current_sum]:
                    all_pair_sum[current_sum].append(pair_values)

    # Final deduplication step
    seen = set()
    final_quads = []
    for quad in quadruplets:
        quad_tuple = tuple(quad)  # Convert to tuple for hashing
        if quad_tuple not in seen:
            seen.add(quad_tuple)
            final_quads.append(list(quad_tuple))

    return final_quads
