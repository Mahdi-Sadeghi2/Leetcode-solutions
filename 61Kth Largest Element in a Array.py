# Time complexity O(nlogn) | Space complexity O(n)
import heapq


def findKthLargest(nums, k) -> int:
    min_heap = []

    for num in nums:
        # Push current number to heap (Python's heapq is min-heap by default)
        heapq.heappush(min_heap, num)  # O(log k)

        # Maintain heap size = k by removing smallest when exceeded
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # O(log k)

    # The root is now the kth largest element
    return min_heap[0]
