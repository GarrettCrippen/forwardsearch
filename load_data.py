import numpy as np
file_name = 'small-test-dataset.txt'

#load data from file
data= np.loadtxt(file_name,delimiter='\t',dtype=str)
print(data[0])