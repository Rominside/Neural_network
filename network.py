import pandas as pd
import json


def act(num):
    if num > 0:
        return num
    else:
        return 0


class Neuron(object):
    def __init__(self, childs, weight, porog, layer):
        self.childs = childs
        self.weight = weight
        self.porog = porog
        self.layer = layer

    def getout(self, input):
        out = 0
        if self.childs is None:
            for i in range(len(input)):
                out += self.weight[i] * input[i]
            out = act(out + self.porog)
        else:
            for i in range(len(self.childs)):
                out += self.weight[i] * self.childs[i].getout(input)
            out = act(out + self.porog)

        if self.layer == 1:
            print(out)

        return out


def preparing_weight():
    with open("weight.json") as jsonFile:
        weight_layers = json.load(jsonFile)

    weight_layers_int = []
    for layer in range(len(weight_layers)):
        weight_layers_int.append([])
        for list_ in range(len(weight_layers[layer])):
            weight_layers_int[layer].append([])
            for item in range(len(weight_layers[layer][list_])):
                weight_layers_int[layer][list_].append([])
                weight_layers_int[layer][list_][item] = (int(weight_layers[layer][list_][item] * 100_000_000))

    return weight_layers_int


def create_net():
    weight_layers = preparing_weight()

    layer_0 = []
    for i in range(9):
        weights = []
        for j in range(9):
            weights.append(weight_layers[0][j][i])
        layer_0.append(Neuron(childs=None, weight=weights, porog=0, layer=0))
        print(weights)

    layer_1 = []
    for i in range(9):
        weights = []
        for j in range(9):
            weights.append(weight_layers[1][j][i])
        layer_1.append(Neuron(childs=layer_0, weight=weights, porog=0, layer=1))

    weights = []
    for i in weight_layers[2][0]:
        weights.append(i)
    layer_2 = Neuron(childs=layer_1, weight=weights, porog=0, layer=2)

    return layer_2


def data_preparation():
    dataset_test = pd.read_csv("Test.txt", sep=",", header=None)

    dataset_test = dataset_test.drop(columns=dataset_test.iloc[:, 9:41])
    dataset_test = dataset_test.drop(columns=42)

    dataset_test.loc[(dataset_test[41] == "normal", 41)] = 0
    dataset_test.loc[(dataset_test[41] != 0, 41)] = 1

    dataset_test.loc[(dataset_test[1] == "tcp", 1)] = 0
    dataset_test.loc[(dataset_test[1] == "udp", 1)] = 1
    dataset_test.loc[(dataset_test[1] == "icmp", 1)] = 2

    i = 0
    for item in pd.unique(dataset_test[2]):
        dataset_test = dataset_test.replace(item, i)
        i += 1
    i = 0
    for item in pd.unique(dataset_test[3]):
        dataset_test = dataset_test.replace(item, i)
        i += 1

    x_test = dataset_test.iloc[:, 0:9]
    y_test = dataset_test.iloc[:, 9:10]

    return {"x_test": x_test, "y_test": y_test}


def test_net():
    x_test = data_preparation()["x_test"]
    y_test = data_preparation()["y_test"]

    network = create_net()

    right = 0
    wrong = 0
    total = 0

    res = [1 if network.getout(input=x_test.T[_].to_list()) > 0 else 0 for _ in range(len(x_test))]
    for _ in range(len(res)):
        if res[_] == y_test[41][_]:
            right += 1
        else:
            wrong += 1
        total += 1

    print("total = ", total)
    print("right = ", right)
    print("wrong = ", wrong)
    print(right * 100 / total)


if __name__ == "__main__":
    test_net()
