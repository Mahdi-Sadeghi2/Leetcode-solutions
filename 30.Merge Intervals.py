# Time complexity O(nlogn) | Space complexity O(n)

def merge(intervals):
    # Handle empty input case
    if not intervals:
        return []

    # Sort intervals based on their start time (O(n log n))
    # This ensures we process intervals in chronological order
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize result list with the earliest interval
    merged_intervals = []
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    # Iterate through remaining intervals (skip first one since we already added it)
    for next_interval in sorted_intervals[1:]:
        # Unpack current and next interval boundaries
        current_start, current_end = current_interval
        next_start, next_end = next_interval

        # Check for overlap between current and next interval
        if current_end >= next_start:
            # Merge overlapping intervals by extending current interval's end time
            current_interval[1] = max(current_end, next_end)
        else:
            # No overlap - move to next distinct interval
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals
