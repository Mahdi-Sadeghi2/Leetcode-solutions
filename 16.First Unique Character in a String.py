# Time complexity O(n) | Space complexity O(n)

def firstUniqChar(s):
    hash_table = {}
    for i in s:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1
    for i in range(len(s)):
        if hash_table[s[i]] == 1:
            return i
    return -1
