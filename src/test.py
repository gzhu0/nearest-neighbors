import algorithm

def read_data(path):
    data = []
    with open(path, "r") as input:
        for line in input:
            line = [float(x) for x in line.split()]
            data.append(line)
    return data

data = read_data("data/data1.txt")
print("read data")

max_score, best_features  = algorithm.forward_search(data)
print(f"Max Score: {max_score}")
print(f"Best Feature Set: {best_features}")
