import numpy as np

arr2 = np.array([[1, 2], [3, 4]])
arr = np.array([1, 2, 3])
result = arr + 5
trans_arr2 = arr2.T
print(trans_arr2)
print(result)
new_arr = np.insert(arr, 1, 10)
print(new_arr)
new_arr3 = np.delete(arr, 1)
print(new_arr3)
new_arr3[1] = 20




