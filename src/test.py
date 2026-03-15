import algorithm
import time
import json

def read_data(path):
    data = []
    with open(path, "r") as input:
        for line in input:
            line = [float(x) for x in line.split()]
            data.append(line)
    return data

#path = "Small_data\CS170_Small_DataSet__1.txt"
path = "Large_data\CS170_Large_DataSet__1.txt"
data = read_data(path)

start = time.perf_counter()
max_score, best_features, search_data = algorithm.forward_search(data)
end = time.perf_counter()
print("Finished Algorithm")
print(f"Max Score: {max_score}")
print(f"Best Feature Set: {best_features}")
print(f"Exectuion Time: {end-start:.2f}")
with open("large_forward.json", "w") as f:
    f.write(json.dumps(search_data))

start = time.perf_counter()
max_score, best_features, search_data = algorithm.backward_search(data)
end = time.perf_counter()
print("Finished Algorithm")
print(f"Max Score: {max_score}")
print(f"Best Feature Set: {best_features}")
print(f"Exectuion Time: {end-start:.2f}")
with open("large_backwards.json", "w") as f:
    f.write(json.dumps(search_data))

# print("Testing NN")
# point = [1,1,1,1]
# data = [
#     [1,5,6,7],
#     [1,3,5,5],
#     [1,5,2,5]
# ]
# features = [1,2]


#data_path = "Small_data\CS170_Small_DataSet__1.txt"
#data_path = "Large_data\CS170_Large_DataSet__1.txt"
# data_path = "data\data1.txt"
# data = read_data(data_path)
# print("read data")

# start = time.perf_counter()
# max_score, best_features, search_data  = algorithm.forward_search(data)
# end = time.perf_counter()
# runtime = end-start

# print(f"Max Score: {max_score}")
# print(f"Best Feature Set: {best_features}")
# print(f"Exectuion Time: {end-start:.2f}")
