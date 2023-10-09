import keras.models
from keras.models import Sequential
import pandas as pd
import tensorflow as tf
import numpy as np


def test_network():
    dataset_train = pd.read_csv("Train.txt", sep=",", header=None)
    dataset_test = pd.read_csv("Test.txt", sep=",", header=None)

    dataset_train = dataset_train.drop(columns=42)
    dataset_test = dataset_test.drop(columns=42)

    dataset_train.loc[(dataset_train[41] == "normal", 41)] = 0
    dataset_train.loc[(dataset_train[41] != 0, 41)] = 1

    dataset_train.loc[(dataset_train[1] == "tcp", 1)] = 0
    dataset_train.loc[(dataset_train[1] == "udp", 1)] = 1
    dataset_train.loc[(dataset_train[1] == "icmp", 1)] = 2

    i = 0
    for item in pd.unique(dataset_train[2]):
        dataset_train = dataset_train.replace(item, i)
        i += 1
    i = 0
    for item in pd.unique(dataset_train[3]):
        dataset_train = dataset_train.replace(item, i)
        i += 1

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

    y_train = dataset_train.iloc[:, 41:42]
    x_train = dataset_train.iloc[:, 0:41]

    y_test = dataset_test.iloc[:, 41:42]
    x_test = dataset_test.iloc[:, 0:41]

    # print(pd.unique(y_train[41]))
    # print(pd.unique(x_train[1]))
    # print(pd.unique(x_train[2]))
    # print(pd.unique(x_train[3]))
    print(x_test)
    print(y_test)

    classifier = Sequential()
    classifier.add(tf.keras.layers.Dense(units=42, activation='relu'))
    classifier.add(tf.keras.layers.Dense(units=42, activation='relu'))
    classifier.add(tf.keras.layers.Dense(units=1, activation='relu'))

    classifier.compile(optimizer='RMSprop', loss='binary_crossentropy')
    y_train = y_train.values.astype(float)
    # x_train = x_train.values.astype(float)
    classifier.fit(x=x_train, y=y_train, batch_size=1, epochs=3)

    classifier.save("model_1")
    classifier_loaded = keras.models.load_model("model_1")
    classifier_loaded.evaluate(x_test, y_test)

    y_pred = classifier.predict(x_test)
    y_pred = [1 if y >= 0.5 else 0 for y in y_pred]

    total = 0
    correct = 0
    wrong = 0
    for i in range(len(y_pred)):
        total = total + 1
        if y_test.at[i, 41] == y_pred[i]:
            correct = correct + 1
        else:
            wrong = wrong + 1

    print("Total " + str(total))
    print("Correct " + str(correct))
    print("Wrong " + str(wrong))


if __name__ == "__main__":
    test_network()
    classifier_loaded = keras.models.load_model("model_1")
    print(classifier_loaded.layers[0].get_weights())
