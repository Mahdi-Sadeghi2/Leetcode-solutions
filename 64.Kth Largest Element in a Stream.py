# Time complexity O(nlogn) | Space complexity O(n)
import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []

        # Initialize the heap with first k elements
        for num in nums:
            self.add(num)  # Using add() to handle initialization

    def add(self, val):
        """
        Add a new score and return the current kth largest score.
        Time: O(log k) for each insertion/removal
        """
        # Push to heap (using a min-heap to track k largest elements)
        heapq.heappush(self.min_heap, val)

        # If heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The kth largest is at the root of the min-heap
        return self.min_heap[0]
