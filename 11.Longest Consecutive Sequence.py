# Time complexity O(n) | Space complexity O(n)

def longest_consecutive(nums):
    # Initialize variables to track the best range found and its length
    best_range = []          # Stores the start and end of longest consecutive sequence
    longest_length = 0       # Stores the length of the longest sequence found

    # Create a hash table (dictionary) to store all numbers for O(1) lookups
    hash_table = {}
    for num in nums:
        # Mark all numbers as unprocessed (True means not yet checked)
        hash_table[num] = True

    # Iterate through each number in the input array
    for num in nums:
        # Skip if this number was already processed as part of another sequence
        if not hash_table[num]:
            continue

        # Mark the current number as processed
        hash_table[num] = False
        # Start counting the sequence length (includes current number)
        current_length = 1
        left = num - 1       # Check for consecutive numbers smaller than current
        right = num + 1      # Check for consecutive numbers larger than current

        # Expand to the left (decreasing numbers) as far as possible
        while left in hash_table:
            hash_table[left] = False  # Mark as processed
            current_length += 1       # Increase sequence length
            left -= 1                 # Move to next smaller number

        # Expand to the right (increasing numbers) as far as possible
        while right in hash_table:
            hash_table[right] = False  # Mark as processed
            current_length += 1       # Increase sequence length
            right += 1                # Move to next larger number

        # Update our record if we found a longer sequence
        if current_length > longest_length:
            longest_length = current_length
            # left+1 because we overshot by 1 in the while loop
            best_range = [left + 1, right - 1]

    # Return the length of the longest consecutive sequence
    return longest_length
