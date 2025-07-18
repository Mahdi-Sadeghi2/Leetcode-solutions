# Time complexity O(n) | Space complexity O(n)
def candy(ratings):
    # Initialize rewards array with 1 candy per child (minimum requirement)
    rewards = [1 for _ in ratings]

    # Left-to-right pass: Ensure right neighbors with higher ratings get more candy
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            # Current child gets 1 more than left neighbor
            rewards[i] = rewards[i-1] + 1

    # Right-to-left pass: Ensure left neighbors with higher ratings get more candy
    # We traverse in reverse to handle dependencies from the right
    for i in reversed(range(len(ratings)-1)):
        if ratings[i] > ratings[i+1]:
            # Take the maximum between current value and right neighbor's candy + 1
            # This preserves left-pass results while satisfying right constraints
            rewards[i] = max(rewards[i], rewards[i+1] + 1)

    # Sum all candies for the minimal valid distribution
    return sum(rewards)
