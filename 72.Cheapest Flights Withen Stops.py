# Time complexity O(E + V * K log (V * K)) | Space complexity O(V + E + V * K)
# Where E is number of edges (flights), V is number of vertices (cities), K is max stops
import heapq


def findCheapestPrice(n, flights, src, dst, k):
    """
    Finds the cheapest price from source to destination with at most k stops using Dijkstra's algorithm.

    Args:
        n: number of cities (vertices)
        flights: list of flight tuples (from, to, price)
        src: source city
        dst: destination city
        k: maximum allowed stops

    Returns:
        The cheapest price or -1 if no valid route exists
    """
   # Build the adjacency list to represent the graph
    # adj[i] contains list of tuples (neighbor, price) for flights from city i
    adj = [[] for _ in range(n)]
    for flight in flights:
        from_i, to_i, price_i = flight
        adj[from_i].append((to_i, price_i))

    # Priority queue (min-heap) for Dijkstra's algorithm
    # Elements are tuples: (current_total_cost, current_city, stops_made_so_far)
    heap = []
    # Start with source city, 0 cost, 0 stops
    heapq.heappush(heap, (0, src, 0))

    # Array to track minimum cost to reach each city with specific number of stops
    # costs[city][stops] = min_cost
    # We only need to track up to k+1 stops (since k is max allowed)
    min_costs = [[float('inf')] * (k+2) for _ in range(n)]
    min_costs[src][0] = 0  # Cost to reach src with 0 stops is 0

    while heap:
        current_cost, current_city, stops = heapq.heappop(heap)

        # If we've reached destination, return the cost (guaranteed to be cheapest)
        if current_city == dst:
            return current_cost

        # Skip if we've already used all our stops
        if stops > k:
            continue

        # Skip if we've found a cheaper way to reach this city with same or fewer stops
        if current_cost > min_costs[current_city][stops]:
            continue

        # Explore all neighboring cities
        for neighbor, price in adj[current_city]:
            new_cost = current_cost + price
            new_stops = stops + 1

            # Only consider this path if it's cheaper than previously found for this stop count
            if new_cost < min_costs[neighbor][new_stops]:
                min_costs[neighbor][new_stops] = new_cost
                heapq.heappush(heap, (new_cost, neighbor, new_stops))

    # If we exhaust all possibilities without finding destination
    # Check all possible stop counts up to k+1 for the destination
    min_price = min(min_costs[dst])
    return min_price if min_price != float('inf') else -1
