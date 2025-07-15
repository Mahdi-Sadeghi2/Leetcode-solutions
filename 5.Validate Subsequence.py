# Time complexity O(n) | Space complexity O(1)

def isSubsequences(s, t):
    """
        :type s: str
        :type t: str
        :rtype: bool
    """
    s = list(s)
    t = list(t)
    str_index = 0
    seq_index = 0
    while str_index < len(t) and seq_index < len(s):
        if t[str_index] == s[seq_index]:
            seq_index += 1
        str_index += 1
    return seq_index == len(s)


print(isSubsequences("acb", "ahbgdc"))
