import numpy as np


def numpy_log(arr: np.ndarray) -> np.ndarray:
    """
    Calculate the natural logarithm of each element in the input NumPy array.


    Parameters:
    arr (np.ndarray): A NumPy array.

    Returns:
    np.ndarray: A NumPy array of the same shape as the input array, where each element is the natural logarithm of the corresponding element in the input array.
    """
    # TODO

    return np.log(arr)


if __name__ == "__main__":
    arr = np.array([0, np.e**4, np.e**6])
    print(numpy_log(arr))
