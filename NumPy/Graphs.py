import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
import numpy as np

"""
#sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
#sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
#plt.show()
"""

arr = np.array([0, 1, 2, 4])
arr = np.append(arr, 6)

print(arr)