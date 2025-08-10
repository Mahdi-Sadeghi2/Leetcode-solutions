# Time complexity O(nlogn) | Space complexity O(n)
import heapq


def mergeKLists(lists):
    # Create a dummy node to build the result
    dummy = ListNode()
    current = dummy

    # Initialize the min-heap
    min_heap = []

    # Push the first node of each list into the heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst.val, i))

    # Process the heap until empty
    while min_heap:
        val, i = heapq.heappop(min_heap)

        # Add the node to the result list
        current.next = ListNode(val)
        current = current.next

        # Move to the next node in the list
        lists[i] = lists[i].next
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i))

    return dummy.next
