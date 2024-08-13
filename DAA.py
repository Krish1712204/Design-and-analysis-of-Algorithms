# NumPy stands for Numerical Python, is an open-source Python library
# It provides support for large, multidimensional arrays and matrices.

import numpy as np


def count_zeroes(arr):
    # Convert the list to a numpy array
    np_arr = np.array(arr)
    # Count the number of zeroes using numpy sum function
    num_of_zeroes = np.sum(np_arr == 0)
    return num_of_zeroes


def is_valid_array(arr):
    # Checking if the array contains all 1s followed by all 0s
    # It does this by sorting the array in reverse order (sorted(arr, reverse=True))
    # and comparing it with the original array (arr).
    # If the sorted array matches the original array, it returns True,
    # indicating that the array is valid. Otherwise, it returns False.

    return arr == sorted(arr, reverse=True)


# Taking input from the user

input_array = input("Enter the elements of the array separated by spaces ")
arr = list(map(int, input_array.split()))

# input_array.split() turns this into ["1", "1", "1", "1", "0", "0"].
# map(int, input_array.split()) converts each of these string elements into integers,
# resulting in a map object.
# list(map(int, input_array.split())) converts the map object into a list,
# producing [1, 1, 1, 1, 0, 0].


if is_valid_array(arr):
    # Output the number of zeroes in the array
    print(f"Number of zeroes in the array: {count_zeroes(arr)}")
else: 
    print("Invalid input: The array must contain all 1s followed by all 0s.")