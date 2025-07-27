# Time complexity O(n) | Space complexity O(1)


class Node:
    """Node class represents a single element in the linked list"""

    def __init__(self, value):
        self.value = value  # The data stored in the node
        self.next = None   # Reference to the next node (None by default)


class SinglyLinkedList:
    """Singly linked list implementation with common operations"""

    def __init__(self):
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list
        self.size = 0     # Number of nodes in the list

    def get(self, index):
        """Get the node at a specific index (0-based)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):  # Traverse until we reach the desired index
            current = current.next
        return current

    def add_at_head(self, value):
        """Add a new node at the beginning of the list"""
        node = Node(value)

        if not self.head:  # If list is empty
            self.tail = node
        else:
            node.next = self.head  # New node points to current head

        self.head = node  # Update head to be the new node
        self.size += 1
        return self  # Return self to allow method chaining

    def add_at_tail(self, value):
        """Add a new node at the end of the list"""
        node = Node(value)

        if not self.head:  # If list is empty
            self.head = node
        else:
            self.tail.next = node  # Current tail points to new node

        self.tail = node  # Update tail to be the new node
        self.size += 1
        return self

    def add_at_index(self, index, value):
        """Insert a new node at a specific index"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            return self.add_at_head(value)
        if index == self.size:
            return self.add_at_tail(value)

        # Insert in the middle
        node = Node(value)
        prev = self.get(index-1)  # Get the node before insertion point
        node.next = prev.next     # New node points to next node
        prev.next = node         # Previous node points to new node
        self.size += 1
        return self

    def delete_at_index(self, index):
        """Remove and return the node at a specific index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:  # Deleting the head
            deleted = self.head
            self.head = self.head.next
            if self.size == 1:  # If list becomes empty
                self.tail = None
        else:
            prev = self.get(index-1)
            deleted = prev.next
            prev.next = deleted.next
            if index == self.size-1:  # If deleting the tail
                self.tail = prev

        self.size -= 1
        return deleted  # Return the deleted node

    def __str__(self):
        """String representation of the linked list for printing"""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"


# Demonstration of the linked list operations
if __name__ == "__main__":
    print("Creating a new linked list...")
    sll = SinglyLinkedList()
    print(f"Initial list: {sll}")  # Empty list

    print("\nAdding elements at head: 3, 2, 1")
    sll.add_at_head(3).add_at_head(2).add_at_head(1)
    print(f"List after additions: {sll}")  # 1 -> 2 -> 3 -> None

    print("\nAdding element at tail: 4")
    sll.add_at_tail(4)
    print(f"List after addition: {sll}")  # 1 -> 2 -> 3 -> 4 -> None

    print("\nInserting element at index 2: 99")
    sll.add_at_index(2, 99)
    print(f"List after insertion: {sll}")  # 1 -> 2 -> 99 -> 3 -> 4 -> None

    print("\nGetting element at index 3")
    node = sll.get(3)
    print(f"Node at index 3 has value: {node.value}")  # 3

    print("\nDeleting element at index 2")
    deleted = sll.delete_at_index(2)
    print(f"Deleted node value: {deleted.value}")  # 99
    print(f"List after deletion: {sll}")  # 1 -> 2 -> 3 -> 4 -> None

    print("\nAttempting to delete at invalid index (10)")
    try:
        sll.delete_at_index(10)
    except IndexError as e:
        print(f"Error: {e}")  # Index out of bounds
