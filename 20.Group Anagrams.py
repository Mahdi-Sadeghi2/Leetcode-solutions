# Time complexity O(n * k log k) | Space complexity O(n * k)
# where n = number of strings, k = max string length
def groupAnagrams(strs):
    # Edge case: empty input list
    if len(strs) == 0:
        return []

    # Create a list of sorted versions of each string
    # Sorting helps identify anagrams (anagrams have the same sorted form)
    # Example: "eat" -> "aet", "tea" -> "aet"
    sorted_strings = [''.join(sorted(s)) for s in strs]

    # Initialize a hash table to group anagrams
    # Key: sorted string (canonical form), Value: list of original anagrams
    hash_table = {}

    # Iterate through each string and its sorted version
    for i in range(len(sorted_strings)):
        current_sorted = sorted_strings[i]
        original_str = strs[i]

        # If the sorted string is already a key in the hash table,
        # append the original string to its group
        if current_sorted in hash_table:
            hash_table[current_sorted].append(original_str)
        else:
            # Otherwise, create a new entry with the sorted string as the key
            hash_table[current_sorted] = [original_str]

    # Return the grouped anagrams as a list of lists
    return list(hash_table.values())
