#reference https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
#reference project2-starter code

import copy
import validator as v
from sklearn import preprocessing 
import numpy as np
import re 

#helper function to create data structure and normalize file
def normalize(file_name):
    data=np.loadtxt(file_name,delimiter='\t',dtype=str)
    f = []
    c= []
    for line in data:
        line = re.split(r'\s+',line.lstrip())
        f.append(line[1:])
        c.append(line[0])

    f = preprocessing.normalize(np.array(f,dtype=float),axis=0)
    return (f,c)

def forward_selection(file_name):
    print('Beginning forward_selection...\n')
    best_set=(0,0)
    #create validator and load data
    loo_validator = v.Validator()
    f,c = normalize(file_name)
    num_features = len(f[0])

    #this is the depth of the tree
    features = ()
    for i in range(1,num_features+1):  

        #stop at local optimum
        best_accuracy=0.0
        #these are the features to add at each depth
        for k in range(1,num_features+1):
            #check the intersection between feature and set of features
            if not k in set(features):

                #create subset of features
                subset = sorted((*features,k))

                #evaluate accuracy of subset of features
                a=loo_validator.validator(f,c,subset)
                print(f'-Using feature(s): {subset} accuracy is {a}%')

                #continue searching the best feature selection
                if a > best_accuracy:
                    best_accuracy = a
                    feature_to_add = k  
        #print(f'adding {feature_to_add}')
        features=sorted((*features,feature_to_add))
        #fin
        if best_accuracy > best_set[1]:
            best_set=(features,best_accuracy)
            print(f"feature(s): {features} was the best, accuracy is {format(best_accuracy,'.3f')}%\n")
        else:
            #return here if you want to stop at local optimum
            print('Warning accuracy has decreased!!!')

    print(f"Finished Search!! The best feature subset is {best_set[0]} which has an accuracy of {format(best_set[1],'.3f')}%")

#same as forward but start from all features and remove one feature at a time
def backward_elimination(file_name):
    print('Beginning backward_elimination...\n')
    
    #create validator and load data
    loo_validator = v.Validator()
    f,c = normalize(file_name)
    num_features = len(f[0])

    #start with all features
    features = sorted((range(1,num_features+1)))
    best_accuracy=loo_validator.validator(f,c,features)
    best_set = (features,best_accuracy)
    print(f'-Using feature(s): {features} accuracy is {best_accuracy}%')
    print(f"feature(s): {features} was the best, accuracy is {format(best_accuracy,'.3f')}%\n")

    #depth of the tree
    for feature in range(1,len(features)):
        best_accuracy=0.0

        #remove a feature from the set
        for feature_remove in features:
            
            if feature_remove in set(features):

                #remove a feature
                cpy = copy.deepcopy(features)
                cpy.remove(feature_remove)

                #evaluate accuracy of feature subset
                a=a=loo_validator.validator(f,c,cpy)
                print(f'-Using feature(s): {cpy} accuracy is {a}%')

                #continue searching the best feature selection
                if a > best_accuracy:
                    best_accuracy = a
                    feature_to_remove = feature_remove  
        features.remove(feature_to_remove)
        if best_accuracy > best_set[1]:
            best_set=(copy.deepcopy(features),best_accuracy)
            print(f"feature(s): {features} was the best, accuracy is {format(best_accuracy,'.3f')}%\n")
        else:
            #return here if you want to stop at local optimum
            print('Warning accuracy has decreased!!!')

    print(f"Finished Search!! The best feature subset is {best_set[0]} which has an accuracy of {format(best_set[1],'.3f')}%")



#----------------------------Test files here-------------------------------



#assigned data
f1= "data\CS170_Spring_2022_Small_data__16.txt"
f2="data\CS170_Spring_2022_Large_data__16.txt"

forward_selection(f2)      
#backward_elimination(f1)     

#starter data
f3 = "data\small-test-dataset.txt"
f4 = "data\Large-test-dataset.txt"

#forward_selection(f4)
#backward_elimination(f3)


