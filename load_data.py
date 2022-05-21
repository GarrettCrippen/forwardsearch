#https://stackoverflow.com/questions/13028120/split-string-by-arbitrary-number-of-white-spaces
#https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value

import numpy as np
import re
from operator import itemgetter
from sklearn import preprocessing
import time
class Classifier():
    
    def __init__(self):
        pass

    #load the whole dataset
    def train(self,f,c):
        Classifier.features = f
        Classifier.classes = c

    #uses row at features[instance_num] as test_feature and all other features as training_features
    def test(self,instance_num,subset):
        start_time = time.time()
        total_datapoints = len(self.features)
        distances = []

        #go through every instance and just use feature subset
        new_features =[]
        for instance in range(total_datapoints):
            features_subset = []
            for feature in subset:
                #only use the subsets ex. feature 1 is at index 0
                features_subset.append(self.features[instance][feature-1])
            new_features.append(features_subset)
        new_features = np.array(new_features, dtype = float)

        #compute distances of point to all of its neighbors
        for i in range(total_datapoints):

            #don't compute against itself
            if i != instance_num:
                #eucledian distance measure
                dist=np.linalg.norm(new_features[instance_num]-new_features[i])
                distances.append((dist, self.classes[i]))

        #sort to find closest neighbor
        distances = sorted(distances, key = itemgetter(0))
        print(f'instance({instance_num+1}) ,\tpredicted: {distances[0][1]} ,\ttime elapsed = {time.time()-start_time}s')
        return distances[0][1]


#find the nearest neighbors accuracy for all instances(leave-one-out) given a subset of features)
class Validator():
    def __init__(self):
        pass

    #NN: Compute the distances of an test_instance to all training_instances, and return the class of the closest training_instance
    #Validator(Leave-One-Out): correct percentage of guesses of NN-Classifier
    def validator(self,features,classes,subset):
        start_time = time.time()
        test= Classifier()
        test.train(features,classes)
        correct=0

        #RUN NN for every point as a test_instance and all others as training
        for i in range(len(classes)):
            if c[i] == test.test(i,subset):
                correct+=1
        accuracy = correct/len(classes)
        print(f'accuracy is: {accuracy}% ,\ttime elapsed = {time.time()-start_time}s')
        return accuracy

    # def validator(self,features,classes,subset):
    #     total_datapoints = len(features)
    #     correct = 0

    #     #go through every instance
    #     new_features =[]
    #     for instance in range(total_datapoints):
    #         features_subset = []
    #         for feature in subset:
    #             #only use the subsets ex. feature 1 is at index 0
    #             features_subset.append(features[instance][feature-1])
    #         new_features.append(features_subset)
    #     features = np.array(new_features, dtype = float)
            
    #     #perform NN classifier for every point, where i is the test_feature
    #     for i in range(total_datapoints):
    #         test_features = features[i]
    #         test_class = classes[i]
    #         distances = []

    #         #find the distance of instance i to instance k
    #         for k in range(total_datapoints):
    #             neighbor_features = features[k]
    #             neighbor_class = classes[k]

    #             #don't find distance to itself
    #             if i!=k:
    #                 #eucledian distance
    #                 dist = np.linalg.norm(test_features - neighbor_features)
    #                 distances.append((dist,neighbor_class))
    #         distances = sorted(distances,key = itemgetter(0))

    #         #validate results
    #         if distances[0][1] == test_class:
    #             correct+=1

    #     accuracy = correct/total_datapoints
    #     print(f'accuracy is: {accuracy}')
    #     return accuracy



f1 = 'small-test-dataset.txt'
f2 = 'Large-test-dataset.txt'
data=np.loadtxt(f1,delimiter='\t',dtype=str)
f = []
c= []
for line in data:
    line = re.split(r'\s+',line[2:])
    f.append(line[1:])
    c.append(line[0])

f = preprocessing.normalize(np.array(f,dtype=float),axis=0)

print('validating NN with feature subset {3,5,7} for small-test-dataset')
v= Validator()
v.validator(f,c,(3,5,7))
