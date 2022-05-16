#reference https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
#reference project2-starter code
import random
import copy

#select one feature at a time
def forward_selection(num_features):
    print('Beginning forward_selection...\n')
    random.seed()
    best_set=(0,0)

    #this is the depth of the tree
    features = ()
    for i in range(1,num_features+1):
        best_accuracy=0.0
        #these are the features to add at each depth
        for k in range(1,num_features+1):
            #check the intersection between feature and set of features
            if not k in set(features):
                #stub evaluation function(random)
                a=round(random.uniform(0,1),3)
                print(f'-Using feature(s): {sorted((*features,k))} accuracy is {a}%')
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

    print(f"Finished Search!! The best feature subset is {best_set[0]} which has an accuracy of {format(best_set[1],'.3f')}%")

#same as forward but start from all features and remove one feature at a time
def backward_elimination(num_features):
    print('Beginning backward_elimination...\n')

    #start with all features
    features = sorted((range(1,num_features+1)))
    best_accuracy=round(random.uniform(0,1),3)
    best_set = (features,best_accuracy)
    print(f'-Using feature(s): {features} accuracy is {best_accuracy}%')
    print(f"feature(s): {features} was the best, accuracy is {format(best_accuracy,'.3f')}%\n")

    #depth of the tree
    for feature in range(1,len(features)):
        random.seed()
        best_accuracy=0.0

        #remove a feature from the set
        for feature_remove in features:
            
            if feature_remove in set(features):
                #stub evaluation function(random)
                a=round(random.uniform(0,1),3)
                cpy = copy.deepcopy(features)
                cpy.remove(feature_remove)
                print(f'-Using feature(s): {cpy} accuracy is {a}%')
                #continue searching the best feature selection
                if a > best_accuracy:
                    best_accuracy = a
                    feature_to_remove = feature_remove  
        features.remove(feature_to_remove)
        if best_accuracy > best_set[1]:
            best_set=(copy.deepcopy(features),best_accuracy)
        print(f"feature(s): {features} was the best, accuracy is {format(best_accuracy,'.3f')}%\n")

    print(f"Finished Search!! The best feature subset is {best_set[0]} which has an accuracy of {format(best_set[1],'.3f')}%")


