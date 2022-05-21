#https://stackoverflow.com/questions/13028120/split-string-by-arbitrary-number-of-white-spaces
#https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value

import numpy as np
import re
from operator import itemgetter

#REMEMBER: split and take subset
class NN_Classifier():
    def __init__(self):
        pass

    #Store all classes + instances
    def train(self,training_instances: list):
        NN_Classifier.training_instances = training_instances

    #Find the distances of a single instance to all other instances, then return class label of smallest distance
    def test(self,test_instance: int):
        test_instance-=1
        distances = []
        test_features = re.split(r'\s+',NN_Classifier.training_instances[test_instance][2:])[1:]
        for neighbor in range(len(NN_Classifier.training_instances)):

            neighbor_instance = re.split(r'\s+',NN_Classifier.training_instances[neighbor][2:])
            neighbor_features = neighbor_instance[1:]
            neighbor_class = neighbor_instance[0]

            #don't find the distance to itself
            if neighbor != test_instance:
                dist = np.linalg.norm(np.array(test_features,dtype=float)-np.array(neighbor_features,dtype=float))
                distances.append((dist, neighbor_class))
        #return the class of the closest 
        distances = sorted(distances,key = itemgetter(0))
        print(f'predicted class for instance ({test_instance+1}) is: {distances[0][1]}') 

#find the nearest neighbors accuracy for all instances(leave-one-out) given a subset of features)
class Validator:
    def __init__(self):
        pass
    def NN(self,data_raw,subset):
        distances = []
        total_datapoints = len(data_raw)
        correct = 0
        data=[]

        #get the subset of features and preserve the class
        for instance in range(len(data_raw)):
            #this is the class
            vals = [re.split(r'\s+',data_raw[instance][2:])[0]]
            for feature in subset:
                #this is an individual feature
                vals.append(re.split(r'\s+',data_raw[instance][2:])[feature])
            data.append(vals)
            
        #Leave each data point out
        for k in range(total_datapoints):

            test_class = data[k][0]
            test_features = data[k][1:]

            for i in range(total_datapoints):
                neighbor_class = data[i][0]
                neighbor_features = data[i][1:]

                #calculate the distance between the points
                if i != k:
                    dist = np.linalg.norm(np.array(test_features,dtype=float)-np.array(neighbor_features,dtype=float))
                    distances.append((dist, neighbor_class))
            distances = sorted(distances,key = itemgetter(0))
            
            if distances[0][1] == test_class:
                correct+=1

        #sort the distances from the neighbors
        print(f'Accuracy is: {correct/total_datapoints}')        

file_name = 'small-test-dataset.txt'
#NN(file_name,subset=(1,2,3,4,5,6,7,8,9,10))
v= Validator()
v.NN(data_raw=np.loadtxt(file_name,delimiter='\t',dtype=str),subset=(3,5,7))

# N = NN_Classifier()
# N.train(np.loadtxt(file_name,delimiter='\t',dtype=str))
# N.test(5)