import pandas as pd


def act(num):
    if num > 0:
        return num
    else:
        return 0


class Neuron(object):
    def __init__(self, childs, weight, porog):
        self.childs = childs
        self.weight = weight
        self.porog = porog

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

        return out


def preparing_weight():
    weight_layers= [
        [[ 0.51796937,  0.06820214,  0.11847848,  0.00774564,  0.06473134,
        -0.06606561, -0.37956023, -0.57441753,  0.316565  ],
       [-0.40593016,  0.12331647, -0.1545542 , -0.3751775 ,  0.15294749,
        -0.13038126, -0.45423755,  0.08082059, -0.34782776],
       [ 0.43687913,  0.11927657, -0.26243937, -0.5015935 , -0.48587805,
        -0.34240955, -0.37697947, -0.21493924, -0.09455084],
       [ 0.55766463,  0.64146614,  0.17329845,  0.32008293,  0.19950338,
         0.19036311,  0.15335318, -0.08973718, -0.06624815],
       [-0.083979  ,  0.39352882, -0.04857534, -0.31702283, -0.13176967,
        -0.5263291 ,  0.6146198 ,  0.07795078, -0.33674654],
       [ 0.4452973 , -0.60339594,  0.6323468 , -0.4023139 ,  0.44388542,
        -0.36688846,  0.7051419 , -0.51064783,  0.24285741],
       [-0.536062  ,  0.4238987 , -0.39225286,  0.5360532 ,  0.1284079 ,
         0.53832674,  0.57702935, -0.30248564,  0.24040818],
       [ 0.23677492, -0.17697872, -0.14701363,  0.28414804,  0.14723098,
         0.40637308, -0.4848474 ,  0.07802988,  0.11675864],
       [-0.3856094 , -0.21033227,  0.32997638, -0.17019159, -0.5582217 ,
        -0.45521086,  0.48947084, -0.15033889,  0.20305991]],

        [[-0.32275876, 0.29718474, -0.42887795, -0.09639674, 0.75697505,
        0.35574237, 0.09760974, 0.1848429, -0.05412975],
        [-0.1206298, 0.7083189, 0.48237255, -0.12820534, -0.09596717,
        -0.62820154, 0.78519475, 0.2668961, 0.4049714],
        [-0.4332627, -0.6772204, -0.4524668, 0.00322473, -0.15273598,
        0.39593485, -0.1603084, 0.51043534, 0.12883414],
        [0.31068182, 0.26290885, -0.27564096, -0.52734125, 0.10414126,
        0.41596714, -0.23463795, -0.43694296, 0.1926622],
        [-0.5763109, -0.1751761, 0.2231915, -0.5206122, -0.37488255,
        -0.18464391, 0.12710556, 0.46502173, -0.27910084],
        [0.4013567, 0.36172774, -0.24925621, -0.2632273, -0.01130938,
        -0.07349794, 0.18186097, 0.18651621, 0.06079718],
        [0.03692445, 0.28371105, -0.18475279, -0.500533, -0.05189091,
        0.45209858, -0.19003719, 0.52947205, 0.11367917],
        [-0.29517692, 0.19072188, -0.51304746, 0.45850018, 0.08107528,
        -0.3702586, -0.4065379, -0.18759717, -0.20752853],
        [0.15392154, -0.21892619, -0.27026856, 0.09913957, 0.45678002,
        -0.48352993, 0.24678606, 0.05254749, 0.21117686]],

        [[0.14264025,
        0.20602356,
        0.62294483,
        -0.5274598,
        0.61604893,
        -0.5720134,
        0.27585557,
        -0.11946924,
        0.17072096]]
    ]

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
        layer_0.append(Neuron(childs=None, weight=weights, porog=0))

    layer_1 = []
    for i in range(9):
        weights = []
        for j in range(9):
            weights.append(weight_layers[1][j][i])
        layer_1.append(Neuron(childs=layer_0, weight=weights, porog=0))

    weights = []
    for i in weight_layers[2][0]:
        weights.append(i)
    layer_2 = Neuron(childs=layer_1, weight=weights, porog=0)

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
