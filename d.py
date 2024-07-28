import scipy.io as scio
import numpy as np
data = scio.loadmat('ACM.mat')
print(type(data))

for key in data.keys():
    print(key)

for value in data.values():
    tmp = np.array(value)
    print(tmp.shape)