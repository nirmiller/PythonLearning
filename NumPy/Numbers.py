import numpy as np
from numpy import random as r

arr = r.randint(100, size = (5))

filter_array = []

for element in arr:
    if element >= 50:
        filter_array.append(True)
    else:
        filter_array.append(False)


print(arr[filter_array])
