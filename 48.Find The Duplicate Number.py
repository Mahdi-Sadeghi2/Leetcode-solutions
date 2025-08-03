# Time complexity O(n) | Space complexity O(1)


def findDuplicate(nums) -> int:
    # Initialize two pointers (hare and tortoise) at the start of the list
    hare = 0
    tortoise = 0

    # Phase 1: Detect if a cycle exists (Floyd's Tortoise and Hare algorithm)
    while True:
        # Hare moves two steps at a time (fast pointer)
        hare = nums[nums[hare]]
        # Tortoise moves one step at a time (slow pointer)
        tortoise = nums[tortoise]

        # If they meet, a cycle is detected
        if hare == tortoise:
            # Phase 2: Find the entrance of the cycle (the duplicate number)
            pointer = 0  # Reset one pointer to the start

            # Move both pointers one step at a time until they meet
            while pointer != tortoise:
                pointer = nums[pointer]
                tortoise = nums[tortoise]

            # The meeting point is the duplicate number
            return pointer
