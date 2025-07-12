def sorted_squared_array(array):
    # Initialize an output array of the same length, filled with 0s as placeholder
    sorted_squares = [0 for _ in array]  # Using _ for unused loop variable

    # Pointers for the smallest (leftmost) and largest (rightmost) values in the input array
    smaller_value_index = 0
    larger_value_index = len(array) - 1

    # Iterate from the end of the output array (to fill largest squares first)
    for index in reversed(range(len(array))):
        smaller_value = array[smaller_value_index]
        larger_value = array[larger_value_index]

        # Compare absolute values to determine which square should be placed at current index
        if abs(smaller_value) > abs(larger_value):
            sorted_squares[index] = smaller_value * smaller_value
            smaller_value_index += 1  # Move left pointer rightward
        else:
            sorted_squares[index] = larger_value * larger_value
            larger_value_index -= 1  # Move right pointer leftward
