
import numpy as np  
from sklearn.utils import resample  
  
def scaleyellow(samples):  
    count = 0.0  
    total = samples.size  
    for colour in samples:  
        if (colour == 0):  
            count += 1.0  
    # print(count)  
    return count / (total - count)  
  
  
blue = (np.ones(1000))  
yellow = (np.zeros(800))  
  
# yellow/blue=0.8  
  
all = np.hstack((blue, yellow))  
scale = 0.0  
iter = 10000  
for i in range(iter):  
    bootstrapSamples = resample(all, n_samples=100, replace=1)  
    # print(bootstrapSamples)  
    tempscale = scaleyellow(bootstrapSamples)  
    scale += tempscale  
print(scale / iter)