# Time complexity O(n) | Space complexity O(1)

def firstUniqChar(s):
  # Step 1: Build a frequency dictionary to count occurrences of each character
    hash_table = {}
    for char in s:
        if char in hash_table:
            hash_table[char] += 1  # Increment count if character exists
        else:
            hash_table[char] = 1   # Initialize count if character is new

    # Step 2: Traverse the string to find the first character with count = 1
    for i in range(len(s)):
        if hash_table[s[i]] == 1:  # Check if current character is unique
            # Return its index immediately (first occurrence)
            return i

    # If no unique character found, return -1 (as per problem requirements)
    return -1
