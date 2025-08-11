# Time complexiyt O(n) | Space complexity O(n)

from collections import deque


def canFinish(numCourses, prerequisites):
    # Initialize adjacency list and indegree array
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    # Build the adjacency list and indegree array
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1

    # Initialize queue with courses having no prerequisites
    queue = deque()
    for course in range(numCourses):
        if indegree[course] == 0:
            queue.append(course)

    # Count of courses that can be taken
    count = 0

    while queue:
        current = queue.popleft()
        count += 1

        # Reduce indegree for neighbors and enqueue if indegree becomes 0
        for neighbor in adj[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return count == numCourses
