# Time complexity O(logn) | Space complexity O(logn)
def isHappy(n):
    seen = set()  # Track previously seen numbers to detect cycles

    # Continue until we reach 1 (happy) or detect a cycle (unhappy)
    while n != 1:
        # Convert the number to a string to iterate over its digits
        digits = str(n)

        # Calculate the sum of the squares of each digit
        n = sum(int(d)**2 for d in digits)

        # If we've seen this number before, it means we're in a cycle (not happy)
        if n in seen:
            return False

        # Add the current number to the set of seen numbers
        seen.add(n)

    # If we exit the loop, n == 1 (happy number)
    return True
