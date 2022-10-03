import numpy as np
import timeit
import numpy.random as random

random.seed(1651)
A0 = random.randn(3, 4)
x0 = random.randn(4)

print(np.shape(A0))
print(np.shape(x0))