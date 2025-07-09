# O(nlogn) time

def two_sum(coins):
    # Sort the coins in ascending order to process them from smallest to largest
    coins.sort()

    # Initialize the current maximum change we can create (starts at 0)
    current_change_created = 0

    # Iterate through each coin in the sorted list
    for coin in coins:
        # If the current coin is greater than (current_change_created + 1),
        # we can't create (current_change_created + 1) as change, so return it
        if coin > current_change_created + 1:
            return current_change_created + 1

        # Otherwise, add the coin to the current_change_created,
        # expanding the range of change we can make
        current_change_created += coin

    # If all coins are processed without gaps, the smallest missing change is
    # (current_change_created + 1)
    return current_change_created + 1
