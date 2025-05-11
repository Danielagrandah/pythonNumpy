import numpy as np


def numpy_sin(arr: np.ndarray) -> np.ndarray:
    """
    Calculate the sine of each element in the input NumPy array.


    Parameters:
    arr (np.ndarray): A NumPy array.

    Returns:
    np.ndarray: A NumPy array of the same shape as the input array, where each element is the sine of the corresponding element in the input array.
    """
    # TODO

    return np.sin(arr)


if __name__ == "__main__":
    arr = np.array([1, np.pi / 3, np.pi / 6])
    print(numpy_sin(arr))
