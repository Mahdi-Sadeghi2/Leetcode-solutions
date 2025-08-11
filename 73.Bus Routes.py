# Time Complexity O(B * S + B^2) | Space Complexity O(B * S + B)
from collections import deque, defaultdict


def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    # Create a mapping from each stop to the list of buses (indices) that go through it
    stop_to_buses = defaultdict(list)
    for bus, stops in enumerate(routes):
        for stop in stops:
            stop_to_buses[stop].append(bus)

    # Initialize a queue for BFS, starting with all buses that have the source stop
    queue = deque()
    visited_buses = set()
    visited_stops = set()

    # Start with all buses that include the source stop
    for bus in stop_to_buses[source]:
        queue.append((bus, 1))
        visited_buses.add(bus)

    while queue:
        current_bus, num_buses = queue.popleft()

        # Check all stops in the current bus's route
        for stop in routes[current_bus]:
            if stop == target:
                return num_buses

            # For each stop, add all buses that haven't been visited yet
            for next_bus in stop_to_buses[stop]:
                if next_bus not in visited_buses:
                    visited_buses.add(next_bus)
                    queue.append((next_bus, num_buses + 1))

    return -1
