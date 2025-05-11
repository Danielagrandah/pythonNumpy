import numpy as np


def numpy_sqrt(arr: np.ndarray) -> np.ndarray: #This defines a function called numpy_sqrt., It takes one argument called arr, which is expected to be a NumPy array (np.ndarray).,  -> np.ndarray means the function is expected to return a NumPy array as well (this is type hinting—it’s optional but helpful).
    """
    Calculate the square root of each element in the input NumPy array.

    Parameters:
    arr (np.ndarray): A NumPy array.

    Returns:
    np.ndarray: A NumPy array of the same shape as the input array, where each element is the square root of the corresponding element in the input array.
    """
    # TODO

    return np.sqrt(arr) # np.sqrt(arr) calculates the square root of each element in the array.

# if __name__ == "__main__": It’s a Python conditional that checks whether your script is being run directly or being imported as a module into another script.
if __name__ == "__main__": 
    arr = np.array([9, 16, 25])
    print(numpy_sqrt(arr))
