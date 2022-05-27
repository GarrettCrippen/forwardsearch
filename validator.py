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
        #print(f'instance({instance_num+1}) ,\tpredicted: {distances[0][1]} ,\ttime elapsed = {time.time()-start_time}s')
        return distances[0][1]


#find the nearest neighbors accuracy for all instances(leave-one-out) given a subset of features)
class Validator():
    def __init__(self):
        pass

    #NN: Compute the distances of an test_instance to all training_instances, and return the class of the closest training_instance
    #Validator(Leave-One-Out): correct percentage of guesses of NN-Classifier
    def validator(self,features,classes,subset):

        test= Classifier()
        test.train(features,classes)
        correct=0

        #RUN NN for every point as a test_instance and all others as training
        for i in range(len(classes)):
            if classes[i] == test.test(i,subset):
                correct+=1
        accuracy = correct/len(classes)
        #print(f'accuracy is: {accuracy}% ,\ttime elapsed = {time.time()-start_time}s')
        
        return accuracy

