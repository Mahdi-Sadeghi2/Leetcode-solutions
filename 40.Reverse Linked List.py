# Time complexity O(n) | Space complexity O(1)

def reverseList(head):
    """
    Reverse a singly linked list in-place.

    Args:
        head (ListNode): The head node of the linked list

    Returns:
        ListNode: The new head of the reversed list
    """
    previous = None  # Previous node starts as None (will be new tail)
    current = head   # Start with current node at head

    while current:
        # Store next node before we overwrite current.next
        next_node = current.next

        # Reverse the link direction
        current.next = previous

        # Move both pointers forward
        previous = current
        current = next_node

    # When loop ends, 'previous' is the new head
    return previous
