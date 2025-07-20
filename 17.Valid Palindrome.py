# Time complexity O(n) | Space complexity O(n)

def isPalindrome(s):
    # Step 1: Clean the input string
    cleaned = []
    for char in s.lower():  # Convert all characters to lowercase for case-insensitive comparison
        if char.isalnum():  # Only keep alphanumeric characters (letters and numbers)
            cleaned.append(char)
    cleaned = ''.join(cleaned)  # Combine the cleaned characters into a string

    # Step 2: Two-pointer palindrome verification
    i, j = 0, len(cleaned) - 1  # Initialize pointers at start and end
    while i < j:  # Continue until pointers meet in the middle
        if cleaned[i] != cleaned[j]:
            return False  # Characters don't match - not a palindrome
        i += 1  # Move left pointer right
        j -= 1  # Move right pointer left

    # If we complete the loop without mismatches, it's a palindrome
    return True
