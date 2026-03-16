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

#path = "data\CS170_Small_DataSet__28.txt"
path = "data\CS170_Large_DataSet__22.txt"
size = "large"
data = read_data(path)

# Find default rate
count = 0
for i in data:
    if i[0] == 1:
        count += 1
if count > len(data)/2: 
    default_rate = round(count/len(data),3)
else:
    default_rate = round((len(data)-count)/len(data),3)

initial_score = algorithm.k_fold_validation(5, data, set(range(1,len(data[0]))))

# search_data = {}
# start = time.perf_counter()
# max_score, best_features, search_data = algorithm.forward_search(data)
# end = time.perf_counter()
# print("Finished Algorithm")
# print(f"Max Score: {max_score}")
# print(f"Best Feature Set: {best_features}")
# print(f"Exectuion Time: {end-start:.2f}")
# with open(f"{size}_forward.json", "w") as f:
#     search_data[0] = [[], default_rate]
#     f.write(json.dumps(search_data))

search_data = {}
start = time.perf_counter()
max_score, best_features, search_data = algorithm.backward_search(data)
end = time.perf_counter()
print("Finished Algorithm")
print(f"Max Score: {max_score}")
print(f"Best Feature Set: {best_features}")
print(f"Exectuion Time: {end-start:.2f}")
with open(f"{size}_backwards.json", "w") as f:
    search_data[0] = [list(range(1, len(data[0]))), initial_score]
    search_data[len(data[0])-1] = [[], default_rate]
    f.write(json.dumps(search_data))

