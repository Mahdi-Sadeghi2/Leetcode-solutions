# Time complexity O(n) | Space complexity O(1)

def deleteDuplicates(head):
    current = head
    while current:
        next_distinct_val = current.next
        while next_distinct_val != None and current.val == next_distinct_val.val:
            next_distinct_val = next_distinct_val.next
        current.next = next_distinct_val
        current = next_distinct_val

    return head
