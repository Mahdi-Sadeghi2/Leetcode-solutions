# Time complexity O(n) | Space complexity O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def check_loop(head):
    """
    Detects and returns the starting node of a cycle in a linked list using Floyd's Tortoise and Hare algorithm.
    Returns None if no cycle exists.

    Algorithm:
    1. Use two pointers, `hare` (fast) and `tortoise` (slow), to detect a cycle.
    2. If they meet, reset one pointer to the head and move both at the same speed until they meet again.
    3. The meeting point is the start of the cycle.
    """

    # Edge cases: empty list or single node with no cycle
    if not head:
        return None
    if not head.next:
        return None

    # Initialize two pointers (hare moves 2x speed, tortoise moves 1x)
    hare = head
    tortoise = head

    # Phase 1: Detect if a cycle exists
    while hare and hare.next:
        hare = hare.next.next  # Hare moves 2 steps
        tortoise = tortoise.next  # Tortoise moves 1 step

        # If they meet, a cycle exists
        if hare == tortoise:
            break

    # If no cycle found (hare reached the end)
    if hare != tortoise:
        return None

    # Phase 2: Find the starting node of the cycle
    pointer = head  # Reset one pointer to the head

    # Move both pointers at the same speed until they meet
    while pointer != tortoise:
        pointer = pointer.next
        tortoise = tortoise.next

    # The meeting point is the start of the cycle
    return tortoise
