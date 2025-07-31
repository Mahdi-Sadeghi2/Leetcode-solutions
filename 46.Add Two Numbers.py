# Time complexity O(max(m,n)) | Space complexity O(max(m,n))


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with:
        self.head = None  # Pointer to first node
        self.tail = None  # Pointer to last node
        self.size = 0     # Track number of nodes

    def add_at_tail(self, val):
        """Add a new node with given value at the end of the list"""
        node = ListNode(val)  # Create new node

        if not self.head:     # If list is empty
            self.head = node  # New node becomes head
            self.tail = self.head  # And also tail (only node)
        else:
            self.tail.next = node  # Link current tail to new node
            self.tail = node       # Update tail to new node

        self.size += 1  # Increment size counter
        return self     # Return self for method chaining


def addTwoNumbers(self, l1, l2):
    """
    Add two numbers represented as reverse-digit linked lists
    Args:
        l1: First number as linked list (digits in reverse)
        l2: Second number as linked list (digits in reverse)
    Returns:
        Sum as a linked list (digits in reverse)
    """
    carry_forward = 0  # Initialize carry to 0
    results = LinkedList()  # Create result list

    # Loop while either list has digits or there's a carry
    while l1 or l2 or carry_forward:
        # Get current digits (0 if list exhausted)
        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0

        # Calculate sum of digits and carry
        sum_list = l1_value + l2_value + carry_forward

        # Store digit (sum mod 10) and update carry (sum divided by 10)
        total = sum_list % 10
        results.add_at_tail(total)
        carry_forward = sum_list // 10

        # Move to next digits (if available)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # Return head of resulting linked list
    return results.head
