import numpy as np


def numpy_exp(arr: np.ndarray) -> np.ndarray:
    """
    Calculate the exponential value of each element in the input NumPy array.


    Parameters:
    arr (np.ndarray): A NumPy array.

    Returns:
    np.ndarray: A NumPy array of the same shape as the input array, where each element is the exponential value of the corresponding element in the input array.
    """

    # TODO

    return np.exp(arr)


if __name__ == "__main__":
    arr = np.array([5, 6, 7])
    print(numpy_exp(arr))
