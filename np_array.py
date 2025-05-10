import numpy as np
# Creating a 1D array from a list 
one_d_array = np.array([1, 2, 3, 4, 5])

# Creating a 2D array from a list of list
two_d_array = np.array([1, 2, 3], [ 4, 5, 6], [7, 8, 9])

#Using Array Attributes
array = np.array([[1, 2, 3], [ 4, 5, 6], [7, 8, 9]])

# Get the shape of thje array 
print("Shape: ", array.shape)

#Get the size of the array
print("Size: ", array.size)

#Get the number of dimensions of the array
print("Number of dimensions: ", array.ndim)

# Get the size in bytes of each element in the array
print("Item size: ", array.itemsize)

# Create a float array from a list
float_array = np.array([1.2, 2.3, 3.4, 4.5], dtype=np.float32)
print("Float array dtype:", float_array.dtype)  # Output: float32

# Create an integer array from a list
int_array = np.array([1, 2, 3, 4, 5], dtype=np.int16)
print("Integer array dtype:", int_array.dtype)  # Output: int16

# Create a complex array from a list
complex_array = np.array([1 + 2j, 2 + 3j, 3 + 4j], dtype=np.complex64)
print("Complex array dtype:", complex_array.dtype)  # Output: complex64

# Create an array and let Numpy infer the data type
mixed_array = np.array([1, 2, 3.5, 4.5])
print("Mixed array dtype:", mixed_array.dtype)  # Output: float64

# Changing the data type of an existing array
new_dtype_array = mixed_array.astype(np.int32)
print("New dtype array:", new_dtype_array)  # Output: [1 2 3 4]
print("New dtype:", new_dtype_array.dtype)  # Output: int32

# Creating an array of zeros with specified dtype
zeros_array = np.zeros((3, 3), dtype=np.uint8)
print("Zeros array with dtype uint8:\n", zeros_array) # Output:[[0 0 0] [0 0 0] [0 0 0]]


# Creating an array from a Python list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)  # Output: [1 2 3 4 5]

# Creating an array from a Python tuple
my_tuple = (6, 7, 8, 9, 10)
my_array = np.array(my_tuple)
print(my_array)  # Output: [ 6  7  8  9 10]

# Creating an array of zeros
my_array = np.zeros((3, 4))
print(my_array)
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Creating an array of ones
my_array = np.ones((2, 3))
print(my_array)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Creating an array with evenly spaced values
my_array = np.arange(0, 10, 2) # why you only used one paor of ()
print(my_array)  # Output: [0 2 4 6 8]

#To access an element in a multidimensional array, we need to specify its position in each dimension.
my_array = np.array([[1, 2], [3, 4], [5, 6]])
print(my_array[1, 0])  # Output: 3

my_array = np.array([1, 2, 3, 4, 5])
my_array[1:4] = [6, 7, 8]
print(my_array)  # Output: [1 6 7 8 5]


## You can convert in the same line or you can use .astype
# Creating an array with a specific data type
my_array = np.array([1, 2, 3], dtype=np.float64)
print(my_array)  # Output: [1. 2. 3.]

# Converting an array to a different data type
my_array = np.array([1, 2, 3], dtype=np.int32)
my_array = my_array.astype(np.float64)
print(my_array)  # Output: [1. 2. 3.]
