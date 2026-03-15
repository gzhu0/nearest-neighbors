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
    return total**(1/2)
        
def nearest_neighbor(point, data,features):
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
        for test_item in test:
            result = nearest_neighbor(test_item, data, features)
            if result[0] == test_item[0]: correct += 1
            total += 1
    return correct/total

#Fix: add a single feature rather than adding all
def forward_search(dataset):
    '''
    Forward Search that searches while adding features
    '''
    features = set() # Current Features to Test
    search = set(range(1,len(dataset[0]))) # Current features to search
    max_score = 0
    best_features = None
    for x in range(len(search)):
        curr_max_score = 0
        curr_best_feature = None
        print(f"On level {x} of the search tree. Current features: {features}")
        for i in search:
            features.add(i)
            score = k_fold_validation(5, dataset, features)
            print(f"Currently testing feature {i}. Score: {score}")
            if score > curr_max_score: 
                curr_max_score = score
                curr_best_feature = i
            features.remove(i)
        if curr_best_feature == None:
            print("Error: No Best Feature Found")
            break
        features.add(curr_best_feature)
        search.remove(curr_best_feature)
        print(f"Selected feature {curr_best_feature}.")
        if curr_max_score > max_score: 
            max_score = curr_max_score
            best_features = features.copy()
    return max_score, best_features            
  
def backward_search(dataset):
    '''
    Backwards serach that searches while removing features
    '''
    features = set(range(1,len(dataset[0])))
    search = set(range(1,len(dataset[0])))
    max_accuracy = 0
    best_features = 0



        