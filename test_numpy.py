from numpy import *
import numpy as np


a=np.random.randint(0, 10, size=10)
b=np.where(a>5,a,-a)
print(b)