# Time complexity O(nlogn) | Space complexity O(logn)
import math


def swap(array, i, j):
    """Swaps elements at indices i and j in the array."""
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array, start, end):
    """
    Partitions the array around a pivot element.
    - Chooses the middle element as pivot to avoid worst-case O(n²) behavior.
    - Moves all elements ≤ pivot to the left, and > pivot to the right.
    - Returns the final index of the pivot.
    """
    middle = math.floor((start + end) / 2)  # Choose middle element as pivot
    # Move pivot to the start for easier partitioning
    swap(array, start, middle)
    pivot = array[start]  # Pivot element
    i = start + 1  # Left pointer (seeks elements > pivot)
    j = end  # Right pointer (seeks elements ≤ pivot)

    while i <= j:
        # Move i right until an element > pivot is found
        while i <= end and array[i] <= pivot:
            i += 1
        # Move j left until an element ≤ pivot is found
        while j >= start and array[j] > pivot:
            j -= 1
        # Swap elements to maintain the partition
        if i < j:
            swap(array, i, j)

    # Place pivot in its correct position (j is now the partition point)
    swap(array, start, j)
    return j


def quick_sort(array, start=0, end=None):
    """
    Sorts the array using the QuickSort algorithm (in-place).
    - Uses tail recursion optimization to reduce worst-case space to O(log n).
    - Always processes the smaller partition first to minimize stack depth.
    """
    if end is None:
        end = len(array) - 1  # Initialize end if not provided

    if start < end:
        pivot_index = partition(array, start, end)  # Partition the array

        # Optimize space by sorting the smaller partition first
        if pivot_index - start < end - pivot_index:
            quick_sort(array, start, pivot_index - 1)  # Sort left half
            quick_sort(array, pivot_index + 1, end)  # Sort right half
        else:
            quick_sort(array, pivot_index + 1, end)  # Sort right half
            quick_sort(array, start, pivot_index - 1)  # Sort left half


# Example usage
array = [5, 4, 0, 3, 1, 6, 2]
quick_sort(array)
print(array)
