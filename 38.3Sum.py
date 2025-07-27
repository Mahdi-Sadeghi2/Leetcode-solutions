# Time complexity O(n^2) | Space complexity O(n) (for sorting)
def threeSum(nums):
    # Sort the array to enable two-pointer technique
    nums.sort()
    triplets = []

    # Iterate through each number as the first element of the triplet
    for i in range(len(nums) - 2):
        # Skip duplicate elements for the first position (i)
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Initialize two pointers: left (next element) and right (end of array)
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Found a valid triplet
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for the right pointer
                # FIXED: Changed nums[left-1] to nums[right-1] to properly skip right duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers inward after finding a valid triplet
                left += 1
                right -= 1

            elif current_sum < 0:
                # Need a larger sum, move left pointer right
                left += 1
            else:
                # Need a smaller sum, move right pointer left
                right -= 1

    return triplets
