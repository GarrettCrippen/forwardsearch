#reference https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
#reference project2-starter code
import random

#select one feature at a time
def forward_selection(num_features):
    random.seed()
    best_set=(0,0)
    #this is the depth of the tree
    features = ()
    for i in range(1,num_features+1):
        best_accuracy=0.0
        a=0
        #these are the features to add at each depth
        for k in range(1,num_features+1):
            #check the intersection between feature and set of features
            if not k in set(features):
                #possible feature selection
                a=round(random.uniform(0,1),3)
                #print(f'feature:{k} accuracy:{a}')
                #continue searching the best feature selection
                if a > best_accuracy:
                    best_accuracy = a
                    feature_to_add = k  
        #print(f'adding {feature_to_add}')
        features=sorted((*features,feature_to_add))
        #fin
        if best_accuracy > best_set[1]:
            best_set=(features,best_accuracy)
        print(f"Using feature(s): {features}      accuracy is {format(best_accuracy,'.3f')}%")

    print(f"\nfeature(s): {best_set[0]} was the best, accuracy is {format(best_set[1],'.3f')}")




forward_selection(5)
