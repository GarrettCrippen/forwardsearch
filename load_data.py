import numpy as np
import re
from operator import itemgetter

file_name = 'small-test-dataset.txt'
distances = []

#load data from file
data= np.loadtxt(file_name,delimiter='\t',dtype=str)

for k in range(1):
    row = re.split(r'\s+',data[k][2:])
    test_class = row[0]
    test_features = row[1:]

    for i in range(len(data)):
        neighbor = re.split(r'\s+',data[i][2:])
        neighbor_class = neighbor[0]
        neighbor_features = neighbor[1:]

        #calculate the distance between the points
        if i != k:
            dist = np.linalg.norm(np.array(test_features,dtype=float)-np.array(neighbor_features,dtype=float))
            distances.append((dist, neighbor_class))

distances = sorted(distances,key = itemgetter(0))
print(distances)
correct = 0
for i in range(25):
    if float(distances[i][1])>1:
        correct+=1
print(correct)        
# row = data[1][2:].split('  ')
# print(row)
# print(row[1:])