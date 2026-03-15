import algorithm
import os
import time
import json

def read_data(path):
    data = []
    with open(path, "r") as input:
        for line in input:
            line = [float(x) for x in line.split()]
            data.append(line)
    return data


print("Nearest Neighbor Feature Selection Algorithm")
path = input("Type in the name of the file to test: ")
if not os.path.isfile(path):
    print("No file exists.")
    exit()

data = read_data(path)

algo_choice = int(input('''Type in the number of the algorithm you want to run.
    1) Forward Selection
    2) Backwards Elimination
'''))
if algo_choice == 1:
    search_algorithm = algorithm.forward_search
elif algo_choice == 2:
    search_algorithm = algorithm.backward_search
else: 
    print("Incorrect input.")
    exit()

feature_count = len(data[0])-1
instance_count = len(data)

print(f"This dataset has {feature_count} features (not including the class attribute), with {instance_count} instances.")
initial_score = algorithm.k_fold_validation(5, data, set(range(1,feature_count+1)))
initial_score = round(initial_score,3)
print(f"Running nearest neighbor with all {feature_count} features, using K-Fold Cross Validation with k = 5, I get an accuracy of {initial_score*100}%")
print("Beginning Search")
start = time.perf_counter()
max_score, best_features, search_data = search_algorithm(data)
end = time.perf_counter()

print()
print(f"Finished Algorithm! The best feature subset is {best_features}, which has an accuracy of {max_score*100:.1f}%")
print(f"Exectuion Time: {end-start:.2f}")