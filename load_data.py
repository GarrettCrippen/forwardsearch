#https://stackoverflow.com/questions/13028120/split-string-by-arbitrary-number-of-white-spaces
#https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value

import numpy as np
import re
from operator import itemgetter

#find the nearest neighbors validator (for all features)
def NNValidator(file_name):
    distances = []
    #load data from file
    data= np.loadtxt(file_name,delimiter='\t',dtype=str)
    total_datapoints = len(data)
    correct = 0

    #Leave each data point out
    for k in range(total_datapoints):
        row = re.split(r'\s+',data[k][2:])
        test_class = row[0]
        test_features = row[1:]

        for i in range(total_datapoints):
            neighbor = re.split(r'\s+',data[i][2:])
            neighbor_class = neighbor[0]
            neighbor_features = neighbor[1:]

            #calculate the distance between the points
            if i != k:
                dist = np.linalg.norm(np.array(test_features,dtype=float)-np.array(neighbor_features,dtype=float))
                distances.append((dist, neighbor_class))
        distances = sorted(distances,key = itemgetter(0))
        
        if distances[0][1] == test_class:
            correct+=1
            #print('correct for: '+str(k))

    #sort the distances from the neighbors
    print(f'Accuracy is: {correct/(total_datapoints-1)}')        

file_name = 'small-test-dataset.txt'
NNValidator(file_name)