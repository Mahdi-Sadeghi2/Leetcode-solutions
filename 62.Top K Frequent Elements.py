import heapq
from collections import defaultdict
# Tme complexity O(nlogn) | Space complexity O(n)


def topKFrequent(nums, k):

    # Step 1: Count frequencies
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    # Step 2: Use min-heap to keep top k elements
    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        # Maintain heap size of k by removing smallest frequency
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract the numbers from the heap
    return [num for (freq, num) in min_heap]
