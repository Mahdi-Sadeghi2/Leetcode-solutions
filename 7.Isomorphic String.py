# Time complexity O(n) | space complexity O(1)

def isIsomorphic(s, t):
    # Two dictionaries to store character mappings from s to t and t to s
    s_hash = {}  # Maps characters from s to corresponding characters in t
    t_hash = {}  # Maps characters from t to corresponding characters in s

    # If lengths differ, strings can't be isomorphic
    if len(s) != len(t):
        return False

    # Iterate through each character pair
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        # If current s character hasn't been mapped yet, create the mapping
        if char_s not in s_hash:
            s_hash[char_s] = char_t

        # If current t character hasn't been mapped yet, create the mapping
        if char_t not in t_hash:
            t_hash[char_t] = char_s

        # Check if mappings are consistent in both directions
        if s_hash[char_s] != char_t or t_hash[char_t] != char_s:
            return False

    # If all checks passed, strings are isomorphic
    return True
