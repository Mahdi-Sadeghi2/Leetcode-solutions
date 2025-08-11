# Time complexity O(n*t) | Space complexity O(n)


def findJudge(n, trust):
    # Edge case: If there's only one person, they are trivially the judge
    if n == 1:
        return 1

    # Initialize a trust count array with size n+1 (1-based indexing)
    # trust_count[i] will store (trust received - trust given) for person i
    trust_count = [0] * (n + 1)

    # Process each trust relationship
    for a, b in trust:
        # Person 'a' gives trust, so decrement their count
        trust_count[a] -= 1
        # Person 'b' receives trust, so increment their count
        trust_count[b] += 1

    # Check each person to find the judge
    for i in range(1, n + 1):
        # The judge must be trusted by everyone else (n-1 people) and trust nobody
        if trust_count[i] == n - 1:
            return i

    # If no judge found, return -1
    return -1
