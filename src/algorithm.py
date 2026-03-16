import time
import numpy as np

'''
Nearest Neighbors Algorithm
'''

def distance(a, b, features):
    '''
    Finds the distance between two points a and b based on a set of features
    '''
    total = 0
    for f in features:
        total += (a[f]-b[f])**2
    return total # Square root is omitted because of relativity
        
def nearest_neighbor_old(point, data,features):
    '''
    Finds the nearest neighbr of a given data point
    '''
    nn = None
    nn_distance = float('inf')
    for d in data:
        curr_distance = distance(point,d,features)
        if curr_distance < nn_distance:
            nn_distance = curr_distance
            nn = d
    return nn      

def nearest_neighbor(point, data,df,features):
    '''
    Finds the nearest neighbr of a given data point
    '''
    point = np.array([point[int(f)] for f in features]) # Convert the point into a numpy array
    df = df - point # Subtract the point from every item
    df = df ** 2 # Square every entry
    df = np.sum(df,axis=1)
    return data[np.argmin(df, axis=0)]


def k_fold_validation(k, dataset, features):
    '''
    Splits the dataset into k parts, and calls nearest neighbors on each of the tests and evaluate accuracy
    '''
    if k <= 1 or k > len(dataset): 
        print("Error: k out of bounds")
        return
    split_size = len(dataset)//k
    correct = 0
    total = 0
    for i in range(k):
        split_index = split_size*i
        if i == k-1: # Handling the end of the dataset
            test = dataset[split_index:]
            data = dataset[0:split_index]
        else: 
            test = dataset[split_index:split_index+split_size]
            data = dataset[0:split_index] + dataset[split_index+split_size:]
        
        # Find the amount of correct for each split

        df = np.array([[d[int(f)] for f in features] for d in data]) # Convert data into a numpy array
        
        for test_item in test:
            result = nearest_neighbor(test_item, data, df, features)
            if result[0] == test_item[0]: correct += 1
            total += 1
    return correct/total

def search_instance(search, features, dataset, search_type):
    """Given an instance of features, tests each possible insertion / removal based on the type
    Args:
        search (set): Set of all features to search through
        features (set): Set of the current features beign used
        dataset (list[list]): 
        search_type (bool): 0 - Forward Selection, 1 - Backwards Elimination
    Returns:
        float, set: The highest score achieved and the best feature
    """
    curr_max_score = 0
    curr_best_feature = None
    for i in search:
        if search_type == 0:
            features.add(i)
        else:
            features.remove(i)
        score = k_fold_validation(5, dataset, features) 
        score = round(score, 3)
        #print(f"Using feature(s) {features} accuracy is {score*100:.1f}%")
        if score > curr_max_score: 
            curr_max_score = score
            curr_best_feature = i
        if search_type == 0:
            features.remove(i)
        else:
            features.add(i)
    return curr_max_score, curr_best_feature

#Fix: add a single feature rather than adding all
def forward_search(dataset):
    '''
    Forward Search that adds the feature that improves accuracy the most
    '''
    search_data = {}
    features = set() # Current Features to Test
    search = set(range(1,len(dataset[0]))) # Current features to search
    max_score = 0
    best_features = None
    for x in range(1,len(search)+1):
        #print(f"On level {x} of the search tree. Current features: {features}")
        
        curr_max_score, curr_best_feature = search_instance(search, features, dataset, 0)

        if curr_best_feature == None:
            print("Error: No Best Feature Found")
            break
        features.add(curr_best_feature)
        search.remove(curr_best_feature)
        search_data[x] = [list(features), curr_max_score] # Store as data
        
        print(f"Feature set {features} was best, accuracy is {curr_max_score*100:.1f}%")
        if curr_max_score > max_score: 
            max_score = curr_max_score
            best_features = features.copy()

    return max_score, best_features, search_data            

def backward_search(dataset):
    '''
    Backwards search that elimates features to improve accuracy
    '''
    search_data = {}
    features = set(range(1,len(dataset[0])))
    search = set(range(1,len(dataset[0]))) # Current features to search
    # Get initial score and best features, which is all of them: 
    max_score = 0
    best_features = None
    for x in range(1,len(search)+1):
        if len(features) <= 1:
            break
        #print(f"On level {x} of the search tree. Current features: {features}")
        curr_max_score, curr_best_feature = search_instance(search, features, dataset, 1)
        if curr_best_feature == None:
            print("Error: No Best Feature Found")
            break
        features.remove(curr_best_feature)
        search.remove(curr_best_feature)
        search_data[x] = ([list(features), curr_max_score]) # Store as data
        print(f"Feature set {features} was best, accuracy is {curr_max_score*100:.1f}%")
        if curr_max_score > max_score: 
            max_score = curr_max_score
            best_features = features.copy()
    return max_score, best_features, search_data  
