NUMPY:
numpy array is less memory allocated, Fast, convinient than python list.
import numpy as np
arr = np.array([[1, 2, 3],[4, 5, 6]],dtype='float/int64/complex')--- Creating a rank 2 Array-----Arrays data types such as lists, tuples, etc.
arr = np.zeros((row,col))
arr = np.ones((row,col))
arr = np.full((row,col),entity, dtype = 'float/int64/complex')
arr = np.arange(start,end,step size)
arr = np.linspace(start,end,total element)
type(arr)/arr.ndim/arr.shape/arr.size/arr.itemsize/arr.dtype--------'numpy.ndarray'/2/(2/raw,3/col)/6(total element)/4/int64
arr1 = arr.reshape(row,col)-----------reshape array
Transpose_arr = arr.T
arr1 = arr.ravel()-------------flatten array
arr1+/-/*//arr2-----------------------(element wise operation happen)
arr1.dot(arr2)--------------------matrix multiplication
arr+1/arr-2/arr*3(arr*=3)/arr**2-------------------------------------------apply on each element
arr.max()/arr.min()/arr.sum()---------------apply on all elements
arr.max(axis=1/axis=0)---------------1 for row_wise and 0 for col_wise

Numpy | mathematical function:
np.all math function(arr)
np.round_(arr, decimals = 0)-------------This mathematical function round an array to the given number of decimals
np.isreal(arr)----------------return True/False
np.conj(arr)

Numpy | String Operations:
np.char.lower(arr)-------------convert all character in lower case
np.char.split(string , sep = ',')------------returns a list of strings
np.char.join('-', string)------------------- returns a string
np.char.count(arr,specific_word)---------return the array with no. with specific_word in that substring
np.char.rfind(arr,specific_word)--------returns the highest index of the substring.If not found then it returns -1

Numpy | Linear Algebra:
np.linalg.matrix_rank(arr)
np.trace(arr)
np.linalg.det(arr)
np.linalg.inv(arr)
np.linalg.matrix_power(arr, 3)

Numpy | Sorting, Searching and Counting:
np.sort(arr, axis = 0/1)---------------sort along the first column/along raw/whole array
np.argmax(arr, axis=0/1/none)-----------indices of max element along column/row/whole array
np.argmin(arr, axis=0/1/none)-----------indices of min element along column/row/whole array
np.count_nonzero(arr, axis=0/1/none)----count nonzero element along column/row/whole array
Random sampling in numpy:
np.random.randint(low = 0, high = 3, size = (row,col))

arr[raw_index][col_index]-------------indexing same as list
arr[np.array([in_1, in_2, in_3])] ------------Indexes are specified inside the np.array method. index start from 0 to n-1 and -n to -1
sliced_arr = arr[raw start:raw end:step size, col start:col end:step size]--------slicing
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]-------------------------------------------slicing by specific row and col index
temp = arr[arr>3]-------------------------------------------------------slicing by condition
np.vstack((a1,a2))--------------------------for vertical stacking
np.hstack((a1,a2))-------------------------for horizontal stacking
np.vsplit(arr,no.)--------------------------for vertical spliting
np.hsplit(arr,no.)--------------------------for horizontal spliting
boolen array = b = arr > 4-------------------b is True/False arrays
arr[b]---------------------------------------array of only True condition element

iteration in array:
for row in a:
    for cell in row:
        print(cell)

for x in np.nditer(arr,order="C/F"):---------'C' for rawwise operation and 'F' for coulmnwise operation
    print(x)

modifying array values:
for x in np.nditer(arr, op_flags = ['readwrite'/'read'/'write']):
    x[...] = 5*x

Iterate two broadcastable arrays concurrently:
for x,y in np.nditer([a1,a2]):
    print(x,y)