# We should consider the !N(factorial)
# for instance if we have 4 elements in the list
# We should do the counting permutations number liek this:
# 4*3*2*1 = 24 elements permutations need.

def permute(nums):
    """
    Generates all possible permutations of a list of numbers using backtracking.
    - Time Complexity: O(n * n!) (n! permutations, each taking O(n) time to copy)
    - Space Complexity: O(n!) to store all permutations (excluding recursion stack)
    """
    permutations = []
    if len(nums) == 0:
        return [[]]  # Edge case: empty list has one permutation (itself)

    def helper(nums, i):
        """
        Recursive helper to generate permutations via swapping.
        - nums: Current state of the list being permuted.
        - i: Current index being fixed in the permutation.
        """
        if i == len(nums) - 1:
            permutations.append(nums[:])  # Base case: full permutation found
            return

        # Explore all possible swaps for the current index `i`
        for j in range(i, len(nums)):
            # Swap to place nums[j] at position `i`
            nums[i], nums[j] = nums[j], nums[i]
            helper(nums, i + 1)  # Recurse to fix the next position
            # Backtrack (restore original state)
            nums[i], nums[j] = nums[j], nums[i]

    helper(nums, 0)  # Start recursion from index 0
    return permutations
