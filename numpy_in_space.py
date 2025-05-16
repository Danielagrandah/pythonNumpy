import numpy as np

from numpy_sqrt import numpy_sqrt
from numpy_exp import numpy_exp
from numpy_sin import numpy_sin
from numpy_cos import numpy_cos
from numpy_log import numpy_log

def numpy_in_space(arr: np.ndarray) -> dict:
    """
    Calculate the square root, exponential value, sine, cosine, and natural logarithm of each element in the input NumPy array.


    Parameters:
    arr (np.ndarray): A NumPy array.

    Returns:
    dict: A dictionary containing the keys 'sqrt', 'exp', 'sin', 'cos', and 'log' respectively, with values being the results of the corresponding calculations.
    """

    # TODO

    result = {
        'sqrt': f"Resultado de sqrt:\n{numpy_sqrt(arr)}",
        'exp': f"Resultado de exp:\n{numpy_exp(arr)}",
        'sin': f"Resultado de sin:\n{numpy_sin(arr)}",
        'cos': f"Resultado de cos:\n{numpy_cos(arr)}",
        'log': f"Resultado de log:\n{numpy_log(arr)}",
    }
    
    return result

if __name__ == '__main__':
    arr = np.array([4, 5, 6])
    print(numpy_in_space(arr))
