# Time complexity O(n) | Space complexity O(n)

import math


def radix_sort(array):
    """
    Sorts an array of integers using Radix Sort (Least Significant Digit variant).

    Args:
        array: List of non-negative integers to be sorted.

    Returns:
        The sorted array. If the input is empty, returns 'empty array'.
    """
    if not array:
        return "empty array"

    # Find the maximum number to determine the number of digits
    greatest_number = max(array)

    # Calculate the number of digits in the greatest number
    if greatest_number == 0:
        number_of_digits = 1
    else:
        number_of_digits = math.floor(math.log10(greatest_number)) + 1

    # Perform counting sort for each digit place (from LSD to MSD)
    for place in range(number_of_digits):
        counting_sort(array, place)

    return array


def counting_sort(array, place):
    """
    Performs Counting Sort on the given array based on the specified digit place.

    Args:
        array: List of integers to be sorted.
        place: Current digit place (0 for units, 1 for tens, etc.).
    """
    output = [0] * len(array)
    temp = [0] * 10  # Temporary count array for digits 0-9
    digit_place = 10 ** place  # 10^place (e.g., 1, 10, 100, ...)

    # Count occurrences of each digit in the current place
    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1

    # Compute cumulative counts (temp[i] = number of elements ≤ i)
    for i in range(1, 10):
        temp[i] += temp[i - 1]

    # Place elements in sorted order (stable sort)
    for j in range(len(array) - 1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]

    # Update the original array with the sorted output
    for i in range(len(array)):
        array[i] = output[i]


# Test case
if __name__ == "__main__":
    arr = [384, 73, 374, 183, 65, 247, 185]
    print("Original array:", arr)
    sorted_arr = radix_sort(arr)
    print("Sorted array:", sorted_arr)
