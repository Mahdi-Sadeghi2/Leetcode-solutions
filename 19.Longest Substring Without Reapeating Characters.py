# Time complexity O(n) | Space complexity O(n)

def lengthOfLongestSubstring(s):
    max_length = 0  # Stores the maximum length found so far
    # Starting index of the current window (substring being considered)
    start = 0
    seen = {}  # Dictionary to store the last seen index of each character

    for i in range(len(s)):
        char = s[i]

        # If character is already seen and its last occurrence is within current window
        if char in seen:
            # Move the start of the window to the right of the previous occurrence
            # of this character, but don't move left (hence the max())
            start = max(start, seen[char] + 1)

        # Update the maximum length if current window is larger
        max_length = max(max_length, i - start + 1)

        # Record/update the last seen index of this character
        seen[char] = i

    return max_length
