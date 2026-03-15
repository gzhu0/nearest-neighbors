import algorithm

def read_data(path):
    data = []
    with open(path, "r") as input:
        for line in input:
            line = [float(x) for x in line.split()]
            data.append(line)
    return data

print("Testing NN")
point = [1,1,1,1]
data = [
    [1,5,6,7],
    [1,3,5,5],
    [1,5,2,5]
]
features = [1,2]


data_path = "Large_data\CS170_Large_DataSet__1.txt"
#data_path = "data\data1.txt"
data = read_data(data_path)
print("read data")

max_score, best_features  = algorithm.backward_search(data)
print(f"Max Score: {max_score}")
print(f"Best Feature Set: {best_features}")
