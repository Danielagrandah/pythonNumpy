import numpy as np


def numpy_cos(arr: np.ndarray) -> np.ndarray:
    """
    Calculate the cosine of each element in the input NumPy array.


    Parameters:
    arr (np.ndarray): A NumPy array.

    Returns:
    np.ndarray: A NumPy array of the same shape as the input array, where each element is the cosine of the corresponding element in the input array.
    """

    # TODO

    return np.cos(arr)


if __name__ == "__main__":
    arr = np.array([1, np.pi / 3, np.pi / 4])
    print(numpy_cos(arr))
